=========================
Minimum Falling Path Sum
=========================

Author Username: DavidMOBrien

Problem: Given a list of lists of integers representing lists at different "levels",
what is the lowest sum we can find if we can only choose one item from each
"level" if you can only select an item underneath the previously chosen item
or an item to the immediate left or right from the item directly underneath our
previously chosen item.

Example: Given input [[1,2,3],[4,5,6],[7,8,9]]
	Can be visualized as:
	[ 1,2,3 ]
	[ 4,5,6 ]
	[ 7,8,9 ]
	Output: 12, because the lowest falling path would be [1,4,7]

Solution: Using a bottom-top approach, we travel from the bottom (end) of our list
calculating at each level what the lowest sum is for each value in the list
by finding the lowest value that it would travel to next.

Source: https://leetcode.com/problems/minimum-falling-path-sum/