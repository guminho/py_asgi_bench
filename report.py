results = []
svc, latency, rps = None, None, None
with open("report.txt") as f:
    for line in f:
        line: str = line.strip()
        if "svc:" in line:
            svc = line.split(":")[1]
        elif "Latency" in line:
            latency = line.split()[1]
        elif "Requests/sec:" in line:
            rps = float(line.split(":")[1])
            results.append((svc, latency, rps))

results.sort(key=lambda x: -x[-1])
rmax = results[0][-1]
width = 30
for svc, latency, rps in results:
    ratio = rps / rmax
    bar = ("#" * int(ratio * width)).ljust(width)
    print(f"{svc:11}:{latency:>8}:{rps:8.1f}|{bar}|{ratio*100:5.1f}")
