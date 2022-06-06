s = 'azcbobobegghakl'
s1 = 'abcbcd'
count = -1
count2 = -1
count3 = -2
substring = ''
size = 0
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
responses = []
for letter in s:
    for element in alphabet:
        count = count + 1
        if letter == element and count >= count2:
            if count < count3:
                substring = str(letter)
                count2 = count
                count3 = count
            else:
                substring = substring + str(letter)
                count2 = count
                count3 = count
        elif letter == element and count < count2:
            count2 = -1
            count3 = count
            substring = str(letter)
    count = -1
    responses.append(substring)
for element in responses:
    if len(element) > size:
        size = len(element)
        response = element
    elif len(element) == size:
        response = response
print('Longest substring in alphabetical order is: ' + response)
