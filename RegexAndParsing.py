#Task

# You are given a string S. Your task is to find the first occurrence of an alphanumeric character in S (read from left to right) that has consecutive repetitions.

# Input Format:
# A single line of input containing the string S.

# Output Format:
# Print the first occurrence of the repeating character. If there are no repeating characters, print -1.
import re
string = input()
#re.search(pattern, string) returns a match object if the pattern is found in the string
m = re.search(r'([a-zA-Z0-9])\1',string)
if m:
    print(m.groups()[0])
else:
    print(-1)

