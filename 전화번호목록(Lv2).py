def solution(phb):
    hmap = {x:1 for x in phb}

    for i in phb:
        tmp = ''

        for j in i:
            tmp += j

            if tmp in hmap and tmp != i:
                return False

    return True

phb = ["119", "97674223", "1195524421"]	
print(solution(phb))