def solution(participant, completion):
    answer = ''
    temp = {}
    
    for i in participant:
        if i in temp:
            temp[i] +=1
        else:
            temp[i] = 1
    
    for i in completion:
        temp[i] -= 1
        
    for person, cnt in temp.items():
        if cnt > 0:
            answer = person
            return answer