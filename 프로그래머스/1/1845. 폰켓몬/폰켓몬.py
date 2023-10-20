def solution(nums):
    answer = 0
    max_num = int(len(nums)/2)
    hash = {}
    
    for i in nums:
        hash[i] = 1
    
    if len(hash)<max_num:
        answer = len(hash)
    else:
        answer = len(hash)-(len(hash)-max_num)
        
    return answer