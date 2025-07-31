# Longest String in List Function

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)

A simple Python function that finds and returns the longest string from a given list of strings. This exercise focuses on list iteration, string length comparison, and conditional logic.

---

## 📖 Challenge Description

Write a function called `longest` that takes a list of strings as a parameter and returns the longest string in the list. If there are multiple strings of the same maximum length, the function returns the first one encountered.

### Example

For the list `["hi", "hiya", "hello", "howdydoody", "hi there"]`, the function should return `"howdydoody"` as it has the maximum length of 10 characters.

---

## 💻 Code Implementation

```python
def longest(strings: list):
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest

if __name__ == "__main__":
    string_list = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(string_list))
```

**Output:**
```
howdydoody
```

---

## 🧠 Algorithm Explanation

The function uses a simple linear search approach:

1. **Initialize** a variable `longest` as an empty string
2. **Iterate** through each string in the input list
3. **Compare** the length of the current string with the current longest string
4. **Update** the longest string if a longer one is found
5. **Return** the longest string found

**Time Complexity:** O(n) where n is the number of strings in the list  
**Space Complexity:** O(1) using only a single variable to track the longest string

---

## 🛠 How to Run

Clone the repo and run:

```bash
python3 longest_string.py
```

Or import the function in your own code:

```python
from longest_string import longest

my_strings = ["python", "programming", "code", "algorithm"]
result = longest(my_strings)
print(f"Longest string: {result}")
```

---

## 🧪 Test Cases

```python
# Test case 1: Basic functionality
strings1 = ["hi", "hiya", "hello", "howdydoody", "hi there"]
print(longest(strings1))  # Output: "howdydoody"

# Test case 2: Multiple strings with same max length
strings2 = ["cat", "dog", "bird", "fish"]
print(longest(strings2))  # Output: "bird" (first occurrence)

# Test case 3: Single string
strings3 = ["python"]
print(longest(strings3))  # Output: "python"

# Test case 4: Empty strings included
strings4 = ["", "a", "ab", "abc"]
print(longest(strings4))  # Output: "abc"
```

---

## ✨ Key Learning Points

* **List iteration:** Understanding how to traverse through list elements
* **String operations:** Using the `len()` function to compare string lengths
* **Conditional logic:** Implementing comparison logic with if statements
* **Variable tracking:** Maintaining state (longest string) throughout iteration
* **Edge case handling:** The algorithm naturally handles empty lists and equal-length strings

---

## 🔍 Alternative Approaches

While the current implementation is clear and efficient, here are other ways to solve this problem:

### Using the `max()` function:
```python
def longest_alternative(strings: list):
    return max(strings, key=len)
```

### Using list comprehension with `max()`:
```python
def longest_comprehension(strings: list):
    return max(strings, key=lambda x: len(x))
```

---

## 🎓 Course Context

This exercise demonstrates fundamental programming concepts including:
- Function definition and parameters
- List manipulation and iteration
- String length comparison
- Variable assignment and updating
- Basic algorithm design

Perfect for beginners learning Python fundamentals and algorithmic thinking.

---

## 📚 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
