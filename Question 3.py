def findheight(s):
    height = 0
    prev_height = 0
    cnt = 0
    for i in range(len(s)):
        if (s[i] == 'U'):
            height += 1
        elif s[i] == 'D':
            height -= 1
        if height == 0 and prev_height < 0:
            cnt += 1
        prev_height = height
    return cnt



n = input()
s = [char for char in input()]
count = 0
for i in s:
    if i != 'U' and i!='D':
        count = 1
    else:
        continue

if count == 0:
    print(findheight(s))
else:
    print("Please provide valid inputs.")