import re
import math
from collections import Counter

def solution(str1, str2):    
    s1 = [str1[x:x+2].lower() for x in range(len(str1)-1) if str1[x:x+2].isalpha()]
    s2 = [str2[x:x+2].lower() for x in range(len(str2)-1) if str2[x:x+2].isalpha()]

    if not s1 and not s2:
        return 65536
    
    c1, c2 = Counter(s1), Counter(s2)
    tmp = sum((c1&c2).values())/sum((c1|c2).values())
    
    return int(65536 * tmp)

def solution1(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)

s1, s2 = "aa1+aa2", "AAAA12"
print(solution(s1, s2))