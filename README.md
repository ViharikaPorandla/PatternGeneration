# 🎨 Number Patterns

This repository contains a simple Python program to generate number patterns. Currently, it includes a function to generate a pyramid pattern of numbers.

## 🔧 Usage

To use the program, run the following code:

```python

def generate_pyramid_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

generate_pyramid_pattern(5)

This will output:

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

📋 Requirements

Python 3.x
