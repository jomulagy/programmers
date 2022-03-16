def solution(phone_book):
    subString = {}
    for num in phone_book:
        for i in range(1,len(num)):
            subString[num[0:i]]=0
    for num in phone_book:
        if num in subString:
            return False

    return True
