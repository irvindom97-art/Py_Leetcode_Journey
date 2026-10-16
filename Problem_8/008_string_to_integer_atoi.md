# LeetCode #8 — String to Integer (atoi)

## 1. Problem information
**Topic:** String indexing, while loops, ASCII digit checks, arithmetic accumulation, min/max.

## 2. Description and example
**Goal:** Solve the problem according to its required input and output format.

For "   -42abc", skip spaces, read the minus sign, parse 42, stop at a, and return -42.

## 3. Initial approach
A straightforward brute-force or direct approach can be easier to understand, but may repeat work or fail to satisfy the required complexity.

## 4. Optimized approach
Skip leading spaces, parse at most one optional sign, consume consecutive ASCII digits, stop at the first other character, and clamp the result.

## 5. Step-by-step walkthrough
For "   -42abc", skip spaces, read the minus sign, parse 42, stop at a, and return -42.

## 6. Python solution
See `../solutions/string_to_integer_atoi.py`.

## 7. Code concepts
String indexing, while loops, ASCII digit checks, arithmetic accumulation, min/max.

## 8. Time and space complexity
Time O(n); extra space O(1).

## 9. Solution comparison
The simpler approach is useful for understanding the task; the optimized approach reduces unnecessary work and follows the intended algorithmic pattern.

## 10. Key takeaway
Parsing order matters: spaces, optional sign, digits, then clamping.

## 11. Conclusion
Focus on the invariant maintained by the algorithm: it is the key to understanding why the solution works.
