# LeetCode #5 — Longest Palindromic Substring

## 1. Problem information
**Topic:** Two pointers, nested functions, slicing, tuple returns.

## 2. Description and example
**Goal:** Solve the problem according to its required input and output format.

For "cbbd", expansion around the gap between the two b characters finds "bb". Stop when boundaries are invalid or characters differ.

## 3. Initial approach
A straightforward brute-force or direct approach can be easier to understand, but may repeat work or fail to satisfy the required complexity.

## 4. Optimized approach
Expand around every possible center, checking both odd-length centers (i,i) and even-length centers (i,i+1).

## 5. Step-by-step walkthrough
For "cbbd", expansion around the gap between the two b characters finds "bb". Stop when boundaries are invalid or characters differ.

## 6. Python solution
See `../solutions/longest_palindromic_substring.py`.

## 7. Code concepts
Two pointers, nested functions, slicing, tuple returns.

## 8. Time and space complexity
Time O(n²); extra space O(1), excluding the returned substring.

## 9. Solution comparison
The simpler approach is useful for understanding the task; the optimized approach reduces unnecessary work and follows the intended algorithmic pattern.

## 10. Key takeaway
Check both even and odd centers; otherwise palindromes such as 'bb' can be missed.

## 11. Conclusion
Focus on the invariant maintained by the algorithm: it is the key to understanding why the solution works.
