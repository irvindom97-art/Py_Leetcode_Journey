import unittest
from solutions.add_two_numbers import ListNode, Solution as Add
from solutions.longest_substring import Solution as Sub
from solutions.median_sorted_arrays import Solution as Median
from solutions.longest_palindromic_substring import Solution as Pal
from solutions.zigzag_conversion import Solution as Zig
from solutions.reverse_integer import Solution as Rev
from solutions.string_to_integer_atoi import Solution as Atoi

def linked(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def values(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out

class TestExercises(unittest.TestCase):
    def test_2(self):
        self.assertEqual(values(Add().addTwoNumbers(linked([2,4,3]), linked([5,6,4]))), [7,0,8])
        self.assertEqual(values(Add().addTwoNumbers(linked([9,9]), linked([1]))), [0,0,1])
    def test_3(self):
        self.assertEqual(Sub().lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(Sub().lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(Sub().lengthOfLongestSubstring(""), 0)
    def test_4(self):
        self.assertEqual(Median().findMedianSortedArrays([1,3], [2]), 2.0)
        self.assertEqual(Median().findMedianSortedArrays([1,2], [3,4]), 2.5)
    def test_5(self):
        self.assertEqual(Pal().longestPalindrome("cbbd"), "bb")
        self.assertEqual(Pal().longestPalindrome("a"), "a")
    def test_6(self):
        self.assertEqual(Zig().convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(Zig().convert("AB", 1), "AB")
    def test_7(self):
        self.assertEqual(Rev().reverse(123), 321)
        self.assertEqual(Rev().reverse(-123), -321)
        self.assertEqual(Rev().reverse(1534236469), 0)
    def test_8(self):
        self.assertEqual(Atoi().myAtoi("   -42"), -42)
        self.assertEqual(Atoi().myAtoi("4193 with words"), 4193)
        self.assertEqual(Atoi().myAtoi("-91283472332"), -2147483648)

if __name__ == "__main__":
    unittest.main()
