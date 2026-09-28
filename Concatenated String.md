# Concatenated String

**Time limit:** 2500 ms  
**Memory limit:** 128 MB  

You are given two strings $A$ and $B$. You want to build a new string $S$ by concatenating $A$ with itself $K$ times. What's the minimum value of $K$ such that $B$ is a subsequence of $S$?

## Standard input
The first line contains a single string $A$.

The second line contains a single string $B$.

## Standard output
Print a single integer, the minimum value of $K$.

## Constraints and notes
* The lengths of $A$ and $B$ are between $1$ and $10^5$
* Both $A$ and $B$ consist only of lowercase letters of the English alphabet
* If $B$ cannot appear as a subsequence of $A$ no matter how large $K$ is, print `-1`.

---

### Example 1

**Input**
```text
aba
aab
```
**Output**
```text
2
```

### Example 2

**Input**
```text
abc
cba
```
**Output**
```text
3
```

### Example 3

**Input**
```text
abbab
aabbba
```
**Output**
```text
2
```

### Example 4

**Input**
```text
abacdaba
aaabbacaab
```
**Output**
```text
3
```