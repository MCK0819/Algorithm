def solution(s):
    
    if s.isdigit() and len(s) in [4,6]:
        answer = True
    else:
        answer = False
    
    return answer