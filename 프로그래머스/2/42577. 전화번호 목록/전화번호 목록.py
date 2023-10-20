def solution(phone_book):
    answer = True
    phone_book_set = set(phone_book)
    phone_book_dict = {} 

    for phone_number in phone_book:
        for i in range(1, len(phone_number)):
            if phone_number[:i] in phone_book_set:
                return False        

    
    return answer