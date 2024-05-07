def solution(s, n):
    ans = ''
    for i in s:
        if i.islower() and ord(i)+n > 122:
            ans += chr(ord(i)+n-122-1+97)
        elif i.isupper() and ord(i)+n > 90:
            ans += chr(ord(i)+n-90-1+65)
        elif i.isupper() or i.islower():
            ans += chr(ord(i)+n)
        else:
            ans += i             
    
    return ans