package main

import (
	"fmt"
	"net/http"
	"strconv"
	"time"

	"github.com/gin-gonic/gin"
)

const NUM_ROUTE = 50
const SLEPT = 10 * time.Millisecond

func reqOk(c *gin.Context) {
	c.String(http.StatusOK, "ok")
}

func viewHTML(c *gin.Context) {
	count, err := strconv.Atoi(c.Param("count"))
	if err != nil {
		c.String(http.StatusBadRequest, "Invalid count")
		return
	}
	time.Sleep(SLEPT)
	content := fmt.Sprintf("<b>Incr %d</b>", count+1)
	c.Data(http.StatusOK, "text/html; charset=utf-8", []byte(content))
}

func viewApi(c *gin.Context) {
	user, err1 := strconv.Atoi(c.Param("user"))
	record, err2 := strconv.Atoi(c.Param("record"))
	if err1 != nil || err2 != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid user or record"})
		return
	}
	time.Sleep(SLEPT)
	content := map[string]interface{}{
		"params": map[string]int{
			"user":   user + 1,
			"record": record + 1,
		},
		"data": "hello world",
	}
	c.JSON(http.StatusOK, content)
}

func main() {
	router := gin.Default()
	for n := 0; n < NUM_ROUTE; n++ {
		router.GET(fmt.Sprintf("/route-%d", n), reqOk)
	}
	router.GET("/html/:count", viewHTML)
	router.GET("/api/users/:user/records/:record", viewApi)

	router.Run(":8000")
	// GOMAXPROCS=1 go run main.go
}
