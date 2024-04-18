from itertools import product

def solution(numbers, target):
    count = 0
    for combination in product([-1, 1], repeat=len(numbers)):
        total = sum(num * sign for num, sign in zip(numbers, combination))
        if total == target:
            count += 1
    return count