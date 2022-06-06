s = 'azcbobobegghakl'
vow = 0
num = -1
for letter in s:
    num = num + 1
    if letter == 'b':
        if num < (len(s) - 2):
            if s[num + 1] == 'o' and s[num + 2] == 'b':
                vow = vow + 1

print('Number of times bob occurs is: ' + str(vow))
