def print_diamond():
    # Upper half (including the middle row)
    for i in range(1, 14):          # we observed 13 rows to reach the widest point
        spaces = abs(13 - i)        # number of leading spaces decreases then increases
        stars = 26 - 2 * spaces     # stars = max width - 2*spaces (max width is 26)
        print(" " * spaces + "*" * stars)
    
    # Lower half (mirror of upper half, excluding the middle row)
    for i in range(12, 0, -1):
        spaces = abs(13 - i)
        stars = 26 - 2 * spaces
        print(" " * spaces + "*" * stars)

# Run the function
print_diamond()