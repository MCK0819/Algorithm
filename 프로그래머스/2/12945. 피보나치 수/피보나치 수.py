def solution(n):
    
    data = [0,1]
    
    for i in range(2, n+1):
        data.append(data[i-1] + data[i-2])
        
    answer = data[-1]%1234567
    
    return answer