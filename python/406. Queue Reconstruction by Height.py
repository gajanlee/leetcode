# https://leetcode.com/problems/queue-reconstruction-by-height/description/

"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""

# 关键是第一个元素降序，第二个升序，或反过来。然后进行插入
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda a: [a[0],-a[1]],reverse = True)
        result = []
        for p in people:
            result.insert(p[1], p)
        return result