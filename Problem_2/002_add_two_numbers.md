# LeetCode #2 — Add Two Numbers

## 1. Problem information
**Topic:** Linked lists, node references, carry, integer division, modulo, dummy nodes.

## 2. Description and example
**Goal:** Solve the problem according to its required input and output format.

Example: [2,4,3] + [5,6,4] produces [7,0,8], representing 342 + 465 = 807. For each position, compute total = x + y + carry, append total % 10, and update carry = total // 10. Continue while either list or carry remains.

## 3. Initial approach
A straightforward brute-force or direct approach can be easier to understand, but may repeat work or fail to satisfy the required complexity.

## 4. Optimized approach
Add digits in reverse-order linked lists one position at a time. Keep a carry and use a dummy head to simplify output construction.

## 5. Step-by-step walkthrough
Example: [2,4,3] + [5,6,4] produces [7,0,8], representing 342 + 465 = 807. For each position, compute total = x + y + carry, append total % 10, and update carry = total // 10. Continue while either list or carry remains.

## 6. Python solution
See `../solutions/add_two_numbers.py`.

## 7. Code concepts
Linked lists, node references, carry, integer division, modulo, dummy nodes.

## 8. Time and space complexity
Time O(max(m,n)); output space O(max(m,n)).

## 9. Solution comparison
The simpler approach is useful for understanding the task; the optimized approach reduces unnecessary work and follows the intended algorithmic pattern.

## 10. Key takeaway
The dummy node avoids special handling for the first result node. The final answer is dummy.next.

## 11. Conclusion
Focus on the invariant maintained by the algorithm: it is the key to understanding why the solution works.
