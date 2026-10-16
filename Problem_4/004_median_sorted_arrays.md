# LeetCode #4 — Median of Two Sorted Arrays

## 1. Problem information
**Topic:** Binary search, partitions, infinity sentinels, tuple swaps, integer division.

## 2. Description and example
**Goal:** Solve the problem according to its required input and output format.

For [1,2] and [3,4], the valid split puts [1,2] on the left and [3,4] on the right. The median is (2+3)/2 = 2.5. Odd total length returns the maximum left value.

## 3. Initial approach
A straightforward brute-force or direct approach can be easier to understand, but may repeat work or fail to satisfy the required complexity.

## 4. Optimized approach
Binary-search a partition in the shorter array. The two left partitions must contain half the values, and their maximum must not exceed either right-side boundary.

## 5. Step-by-step walkthrough
For [1,2] and [3,4], the valid split puts [1,2] on the left and [3,4] on the right. The median is (2+3)/2 = 2.5. Odd total length returns the maximum left value.

## 6. Python solution
See `../solutions/median_sorted_arrays.py`.

## 7. Code concepts
Binary search, partitions, infinity sentinels, tuple swaps, integer division.

## 8. Time and space complexity
Time O(log(min(m,n))); extra space O(1).

## 9. Solution comparison
The simpler approach is useful for understanding the task; the optimized approach reduces unnecessary work and follows the intended algorithmic pattern.

## 10. Key takeaway
For an even number of values, average the greatest left-side value and smallest right-side value.

## 11. Conclusion
Focus on the invariant maintained by the algorithm: it is the key to understanding why the solution works.
