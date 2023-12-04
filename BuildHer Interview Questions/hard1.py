from collections import deque

def maxSlidingWindow(nums, k):
    result = []
    window = deque()

    for i in range(len(nums)):
        # Remove elements outside the current window
        while window and window[0] < i - k + 1:
            window.popleft()

        # Remove elements smaller than the current element from the back
        while window and nums[window[-1]] < nums[i]:
            window.pop()

        # Add the current index to the window
        window.append(i)

        # Append the maximum element of the current window to the result
        if i >= k - 1:
            result.append(nums[window[0]])

    return result

# Test cases
print(maxSlidingWindow([1], 1))  # Output: [1]
print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Output: [3, 3, 5, 5, 6, 7]
