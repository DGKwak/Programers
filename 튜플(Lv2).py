s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s = s[2:len(s)-2].split('},{')
s.sort(key=len)

print(s)