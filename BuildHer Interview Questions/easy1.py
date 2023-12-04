def length_of_last_word(p):
    p = p.rstrip()
    length_in_last_word = 0

    for char in reversed(p):
        if char == ' ':
            break
        length_in_last_word += 1
    
    return length_in_last_word

# Example 1
p1 = "Hello World"
result1 = length_of_last_word(p1)
print(f"Example 1: The length of the last word is: {result1}")

# Example 2
p2 = "   fly me   to   the moon  "
result2 = length_of_last_word(p2)
print(f"Example 2: The length of the last word is: {result2}")

# Example 3
p3 = "luffy is still joyboy"
result3 = length_of_last_word(p3)
print(f"Example 3: The length of the last word is: {result3}")

