def longestCommonPrefix(input_strings):
     
    length = len(input_strings)
    if (length == 0):
        return ""
    if (length == 1):
        return a[0]
    input_strings.sort()
    ending = min(len(input_strings[0]), len(input_strings[length - 1]))

    i = 0
    while (i < ending and
           input_strings[0][i] == input_strings[length - 1][i]):
        i += 1
 
    prefix = input_strings[0][0: i]
    
    return prefix




input_strings = list(map(str,input().split(",")))
print(longestCommonPrefix(input_strings))