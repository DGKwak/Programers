def solution(elements):
    rslt = set(elements)
    length = len(elements)
    
    for i in range(2, length+1):
        for j in range(length):
            if j+i > length:
                rslt.add(sum(elements[j:])+sum(elements[:j+i-length]))
            else:
                rslt.add(sum(elements[j:j+i]))
        
    return len(rslt)

def solution1(elements):
    rslt = set()

    el_len = len(elements)
    elements = elements * 2

    for i in range(el_len):
        for j in range(el_len):
            rslt.add(sum(elements[j:j+i+1]))

    return len(rslt)

elements = [7,9,1,1,4]
print(solution1(elements))