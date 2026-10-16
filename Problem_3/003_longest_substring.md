# LeetCode #3 — Longest Substring Without Repeating Characters

## 1. Problem information
**Topic:** Hash maps, enumerate, sliding window, indexes, max.

## 2. Description and example
**Goal:** Solve the problem according to its required input and output format.

For "abba", the window grows to "ab"; when the second b appears, move the left boundary past the previous b. The longest valid window has length 2.

## 3. Initial approach
A straightforward brute-force or direct approach can be easier to understand, but may repeat work or fail to satisfy the required complexity.

## 4. Optimized approach
Use a sliding window and a dictionary of each character's latest index.

## 5. Step-by-step walkthrough
For "abba", the window grows to "ab"; when the second b appears, move the left boundary past the previous b. The longest valid window has length 2.

## 6. Python solution
See `../solutions/longest_substring.py`.

## 7. Code concepts
Hash maps, enumerate, sliding window, indexes, max.

## 8. Time and space complexity
Time O(n); space O(k), where k is the number of distinct characters.

## 9. Solution comparison
The simpler approach is useful for understanding the task; the optimized approach reduces unnecessary work and follows the intended algorithmic pattern.

## 10. Key takeaway
Only move the left boundary forward, and move it only when the repeated character is inside the current window.

## 11. Conclusion
Focus on the invariant maintained by the algorithm: it is the key to understanding why the solution works.
