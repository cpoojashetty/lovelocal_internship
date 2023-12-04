from collections import deque

def maxSlidingWindow(m, k):
    result = []
    w = deque()

    for i in range(len(m)):
        # Remove elements outside the current window
        while w and w[0] < i - k + 1:
            w.popleft()

        # Remove elements smaller than the current element from the back
        while w and m[w[-1]] < m[i]:
            w.pop()

        # Add the current index to the window
        w.append(i)

        # Append the maximum element of the current window to the result
        if i >= k - 1:
            result.append(m[w[0]])

    return result

# Test cases
print(maxSlidingWindow([1], 1))  # Output: [1]
print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Output: [3, 3, 5, 5, 6, 7]
