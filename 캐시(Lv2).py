def solution(cacheSize, cities):
    ans = 0
    buff = []
    cities = [x.lower() for x in cities]
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for city in cities:
        if city in buff:
            buff.remove(city)
            buff.append(city)
            
            ans += 1
            
        else:
            if len(buff) == cacheSize:
                buff.pop(0)
                buff.append(city)
                
            else:
                buff.append(city)
                
            ans += 5
    
    return ans