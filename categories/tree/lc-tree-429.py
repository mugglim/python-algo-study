"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []

        ans = [[root.val]]
        queue = deque([[root]])

        while queue:
            adjs = queue.popleft()
            tmp_adjs = []
            tmp_vals = []

            for adj in adjs:
                for child in adj.children:
                    tmp_adjs.append(child)
                    tmp_vals.append(child.val)

            if tmp_adjs:
                queue.append(tmp_adjs)
                ans.append(tmp_vals)

        return ans





