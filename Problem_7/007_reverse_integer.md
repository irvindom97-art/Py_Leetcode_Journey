# LeetCode #7 — Reverse Integer

## 1. Problem information
**Topic:** abs, string slicing [::-1], int conversion, conditional expressions.

## 2. Description and example
**Goal:** Solve the problem according to its required input and output format.

For -120, reverse the magnitude '120' to '021', parse it as 21, and restore the sign to get -21. Return 0 if the result is outside [-2³¹, 2³¹−1].

## 3. Initial approach
A straightforward brute-force or direct approach can be easier to understand, but may repeat work or fail to satisfy the required complexity.

## 4. Optimized approach
Save the sign, reverse the absolute value's digits, restore the sign, and check the signed 32-bit range.

## 5. Step-by-step walkthrough
For -120, reverse the magnitude '120' to '021', parse it as 21, and restore the sign to get -21. Return 0 if the result is outside [-2³¹, 2³¹−1].

## 6. Python solution
See `../solutions/reverse_integer.py`.

## 7. Code concepts
abs, string slicing [::-1], int conversion, conditional expressions.

## 8. Time and space complexity
Time O(d); space O(d), where d is the number of digits.

## 9. Solution comparison
The simpler approach is useful for understanding the task; the optimized approach reduces unnecessary work and follows the intended algorithmic pattern.

## 10. Key takeaway
Python integers do not overflow automatically, so enforce the problem's 32-bit bounds explicitly.

## 11. Conclusion
Focus on the invariant maintained by the algorithm: it is the key to understanding why the solution works.
