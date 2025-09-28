# Stage 1: Builder
FROM golang:1.25-alpine AS builder

WORKDIR /app

# Download dependencies
COPY fwk/gin_/go.mod fwk/gin_/go.sum ./
RUN go mod download

COPY fwk/gin_/main.go .

# Build the app
# -ldflags: strip debugging symbol, reduce binary size
# -a -installsuffix netgo: use pure Go DNS resolver
# CGO_ENABLED=0 (implicitly by -installsuffix): no rely on C libraries
RUN go build -ldflags="-s -w" -a -installsuffix netgo -o /usr/local/bin/webgin .


# Stage 2: Final - The Runtime
FROM alpine:3.22

RUN apk add --no-cache ca-certificates

WORKDIR /root/

COPY --from=builder /usr/local/bin/webgin .

EXPOSE 8000
CMD ["./webgin"]