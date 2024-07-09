def count(s):
    count=0
    for i in range(len(s)):
        if s[i]!=" " and s[i]!="-":
            count+=1
        else:
            continue
    return count

st=input()#enter the number in words
print(count(st))
