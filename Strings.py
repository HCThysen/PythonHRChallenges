# Consider the following:

# A string, s, of length n.
# An integer, k, where  is a factor of k.
# We can split s into n/k substrings where each subtring, t_i, consists of a contiguous block of k characters in s. Then, use each t_i to create string u_i such that:

# The characters in u_i are a subsequence of the characters in t_i.
# Any repeat occurrence of a character is removed from the string such that each character in u_i occurs exactly once. In other words, if the character at some index j in t_i occurs at a previous index < j in t_i, then do not include the character in string .
# Given s and k, print n/k lines where each line i denotes string u_i.

def merge_the_tools(string, k):
    for i in range(len(string)//k):
        subString = ""
        for w in range(k*i,k*(i+1)):
            letter = string[w]
            if letter not in subString:
                subString = subString + letter       
        print(subString)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
