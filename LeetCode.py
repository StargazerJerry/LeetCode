from LinkList import *
from typing import *



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = {}

        def dfs(i, remain):
            #out of range
            if remain <= 0:
                return 0
            if i == len(cost):
                return float("inf")
            if (i, remain) in dp:
                return dp[(i, remain)]


            paint = cost[i] + dfs(i+1, remain - 1 - time[i])
            skip = dfs(i+1, remain)

            #print(i + ", " + remain + "=" + paint + ", " + skip)
            print(f"i={i}, remain={remain} =  paint={paint}, skip={skip}")
            dp[(i, remain)] = min(paint, skip)

            return dp[(i, remain)]
        result = dfs(0, len(cost))
        print()
        print(dp)

        return result

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class MultiaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert(self, parent_value, child_value):
        parent_node = self._find_node(self.root, parent_value)
        if parent_node:
            child_node = TreeNode(child_value)
            parent_node.children.append(child_node)
        else:
            print(f"Parent node with value {parent_value} not found.")

    def _find_node(self, current_node, target_value):
        if current_node.value == target_value:
            return current_node
        for child in current_node.children:
            node = self._find_node(child, target_value)
            if node:
                return node
        return None

    def display(self, node=None, level=0):
        if not node:
            node = self.root
        print("  " * level + str(node.value))
        for child in node.children:
            self.display(child, level + 1)

solu = Solution()

cost = [2,3,4,2]
time = [1,1,1,1]
result = solu.paintWalls(cost, time)
#print(result)