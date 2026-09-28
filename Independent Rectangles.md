# Independent Rectangles

**Time limit:** 1500 ms

**Memory limit:** 128 MB

You are given $N$ rectangles and for each rectangle $i$ you know its width $w_i$ and its height $h_i$.

We call a rectangle $i$ to be *independent* if there is no other rectangle $j$ such that $w_i < w_j$ and $h_i < h_j$.

Count the number of independent rectangles.

## Standard input

The first line contains a single integer $N$.

Each of the following $N$ lines contains two values $w$ and $h$ representing the width and the height of a rectangle.

## Standard output

Output a single number representing the number of independent rectangles.

## Constraints and notes

* $1 \le N \le 10^5$
* $1 \le w_i, h_i \le 10^6$

### Example 1

**Input**

```
5
1 5
2 2
2 3
2 5
3 4
```

**Output**

```
3
```

### Example 2

**Input**

```
6
3 3
3 4
4 3
4 4
1 7
5 8
```

**Output**

```
1
```