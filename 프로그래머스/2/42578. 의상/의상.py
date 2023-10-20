def solution(clothes):
    clothes_dict = {}
    for cloth in clothes:
        category = cloth[1]
        if category in clothes_dict:
            clothes_dict[category] += 1
        else:
            clothes_dict[category] = 1
    
    answer = 1
    for count in clothes_dict.values():
        answer *= (count + 1)

    answer -= 1

    return answer