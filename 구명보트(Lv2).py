def solution(people, limit):
    ans = 0
    people.sort(reverse=True)
    
    left, right = 0, len(people)-1
    
    while left < right:
        if people[left] + people[right] <= limit:
            right -= 1
            ans += 1
        
        left += 1      
    
    return len(people) - ans

people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))