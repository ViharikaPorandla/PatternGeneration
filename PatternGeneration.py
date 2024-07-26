def generate_pyramid_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Example usage
generate_pyramid_pattern(5)
