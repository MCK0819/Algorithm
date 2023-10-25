def solution(progresses, speeds):
    answer = []
    
    while speeds:
        
        for i, speed in enumerate(speeds):
            progresses[i] += speed
            
        count = 0
        
        while progresses and progresses[0] >= 100:
            del progresses [0], speeds[0]
            count += 1
        
        if count > 0:
            answer.append(count)
    
    return answer