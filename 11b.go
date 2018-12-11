package main

import (
	"fmt"
	"strconv"
	"sync"
)

const (
	serialN = 5235
)

func pLvl(x, y int) int {
	plvl := (((x + 10) * y) + serialN) * (x + 10)
	if plvl > 99 {
		s := strconv.Itoa(plvl)
		a, _ := strconv.Atoi(s[len(s)-3 : len(s)-2])
		return a - 5
	}
	return plvl - 5
}

func maxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxGridSum(grid map[int]map[int]int, x, y, maxGridSize int) (int, int) {
	sum, maxVal, maxSize := grid[y][x], 0, 0
	for s := 0; s < maxGridSize; s++ {
		for yi := 0; yi < s+1; yi++ {
			for xi := 0; xi < s+1; xi++ {
				if xi == s || yi == s {
					sum += grid[y+yi][x+xi]
				}
			}
		}
		if sum > maxVal {
			maxVal = sum
			maxSize = s + 1
		}
	}
	return maxVal, maxSize
}

type Stats struct {
	X, Y int
	Size int
	Max  int
}

func solve() {
	grid := make(map[int]map[int]int, 300)
	for y := 1; y < 301; y++ {
		grid[y] = make(map[int]int, 300)
		for x := 1; x < 301; x++ {
			grid[y][x] = pLvl(x, y)
		}
	}

	channel := make(chan Stats, 100)
	var wg sync.WaitGroup

	for y := 1; y < 301; y++ {
		for x := 1; x < 301; x++ {
			wg.Add(1)
			go func(x, y int, ch chan Stats, wg *sync.WaitGroup) {
				defer wg.Done()
				maxSize, maxValue, maxX, maxY, value := 0, 0, 0, 0, 0
				value, size := maxGridSum(grid, x, y, 300-maxInt(x, y))
				if value > maxValue {
					maxValue = value
					maxSize = size
					maxX = x
					maxY = y
				}
				ch <- Stats{
					X:    maxX,
					Y:    maxY,
					Size: maxSize,
					Max:  maxValue,
				}
			}(x, y, channel, &wg)
		}
	}
	maxStat := Stats{
		Max: -999990,
	}

	go func() {
		wg.Wait()
		close(channel)
	}()

	for stat := range channel {
		if stat.Max > maxStat.Max {
			maxStat = stat
		}
	}
	fmt.Println(maxStat.X, maxStat.Y, maxStat.Size)
}

func main() {
	solve()
}
