# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/468370?language=python3

def solution(message, spoiler_ranges):
    answer = 0
    word_list = message.split()
    spoiler_word = []
    
    word_start_list = []
    tmp = 0
    
    for x in word_list:
        word_start_list.append(tmp)
        tmp += len(x) + 1
    
    for y in spoiler_ranges:
        spoiler_len = y[1] - y[0] + 1
        
        tmp = []
        for idx in range(len(word_list)):
            start_num = word_start_list[idx]
            end_num = start_num + len(word_list[idx]) - 1
            
            if y[0] >= start_num and end_num >= y[0]:
                tmp.append(idx)
            
            if y[1] >= start_num and end_num >= y[1]:
                tmp.append(idx)
        
        if tmp[0] == tmp[1]:
            spoiler_word.append(word_list[tmp[0]])
        else:
            spoiler_word.append(word_list[x] for x in tmp)