pastletter = 0
substring = ''
responses = []
for letter in s:
    if pastletter > ord(letter):
        responses.append(substring)
        substring = letter
    else:
        substring = substring + letter
    pastletter = ord(letter)
responses.append(substring)
print('Longest substring in alphabetical order is:', max(responses, key = len))
