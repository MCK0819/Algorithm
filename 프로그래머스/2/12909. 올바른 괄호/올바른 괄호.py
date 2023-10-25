def solution(s):
    stack = 0
    
    for num in s:
        if num in '(':
            stack += 1
        elif num in ')':
            stack -= 1
        if stack < 0:
            return False
    if stack != 0 :
        return False
            
    
    return True