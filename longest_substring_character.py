#Longest Substring without repeating character solution


s = "abcabcbb"
newString = ""
maxLength = 0

for c in s:
    if newString.find(c) == -1:
        newString = newString + c
    else:
        if maxLength < len(newString):
            maxLength = len(newString)
        newString = newString[newString.find(c)+1:]
        newString = newString + c
            

if maxLength < len(newString):
    maxLength = len(newString)

print(maxLength)