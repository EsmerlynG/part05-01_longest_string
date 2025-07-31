# Write your solution here
def longest(strings: list):
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string

    return longest
if __name__ == "__main__":
    string_list = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(string_list))