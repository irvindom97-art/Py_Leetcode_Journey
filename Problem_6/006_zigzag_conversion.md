# LeetCode #6 — Zigzag Conversion

## 1. Problem information
**Topic:** Lists, strings, join, loop state, early returns.

## 2. Description and example
**Goal:** Solve the problem according to its required input and output format.

For "PAYPALISHIRING" with 3 rows, row buffers become "PAHN", "APLSIIG", and "YIR". Joining them produces "PAHNAPLSIIGYIR".

## 3. Initial approach
A straightforward brute-force or direct approach can be easier to understand, but may repeat work or fail to satisfy the required complexity.

## 4. Optimized approach
Simulate row movement and append each character to its row buffer. Reverse direction at the first and last rows.

## 5. Step-by-step walkthrough
For "PAYPALISHIRING" with 3 rows, row buffers become "PAHN", "APLSIIG", and "YIR". Joining them produces "PAHNAPLSIIGYIR".

## 6. Python solution
See `../solutions/zigzag_conversion.py`.

## 7. Code concepts
Lists, strings, join, loop state, early returns.

## 8. Time and space complexity
Time O(n); space O(n).

## 9. Solution comparison
The simpler approach is useful for understanding the task; the optimized approach reduces unnecessary work and follows the intended algorithmic pattern.

## 10. Key takeaway
A single row, or at least as many rows as characters, leaves the string unchanged.

## 11. Conclusion
Focus on the invariant maintained by the algorithm: it is the key to understanding why the solution works.
