import re

def solution(new_id):
    ans = new_id.lower()
    ans = re.sub('[^a-z0-9\-_\.]', '', ans)
    ans = re.sub('\.+', '.', ans)
    ans = re.sub('^[\.]|[\.]$', '', ans)

    if len(ans) == 0:
        ans = 'a'
    else:
        ans = ans[:15]
        ans = re.sub('^[\.]|[\.]$', '', ans)

    if len(ans) < 3:
        ans = ans + ''.join(ans[-1] for _ in range(3-len(ans)))
    
    return ans

s = "...!@BaT#*..y.abcdefghijklm"

print(solution(s))