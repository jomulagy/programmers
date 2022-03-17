from collections import Counter

def solution(clothes):
    answer =1
    list_ = [clothe[1] for clothe in clothes]
    category = Counter(list_)
    
    for clothe in category.keys():
        answer *= (category[clothe]+1)
    return answer-1
