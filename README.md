
# EASY
## Function: length_of_last_word(p)
 Input: A string p<br>
 Output: Returns the length of the last word in the input string./
## How it Works
The input string is first stripped of trailing whitespaces using strip().<br>
A loop iterates over the reversed characters of the string until a space is encountered, counting the length of the last word.<br>
The length of the last word is returned.

# HARD
## Function: maxSlidingWindow(nums, k)
Input:<br>
nums: A list of integers representing the input array.<br>
k: An integer representing the size of the sliding window.<br>
Output:Returns a list containing the maximum element in each sliding window.
## How it Works
The function uses a deque (window) to efficiently keep track of the indices of elements in the current window.<br>
It iterates through the input array, maintaining the window and updating it for each element.<br>
The deque is designed to store indices such that elements outside the current window are removed efficiently.<br>
The result list is populated with the maximum element of each sliding window.

# MEDIUM 
## Function: lowestCommonAncestor(root, p, q)
Inputs:<br>
root: The root node of the binary search tree.<br>
p: The first node.<br>
q: The second node.<br>
Output: Returns the lowest common ancestor of nodes p and q in the binary search tree.

## How it Works
The function recursively traverses the BST based on the values of nodes p and q.<br>
If both nodes are smaller than the current root, the LCA is in the left subtree.<br>
If both nodes are larger than the current root, the LCA is in the right subtree.<br>
If one node is on the left and the other is on the right, the current root is the LCA.<br>
The LCA is found by comparing values and traversing the tree accordingly.

