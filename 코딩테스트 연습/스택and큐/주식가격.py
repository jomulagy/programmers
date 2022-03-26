from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        cur = prices.popleft()
        count=0
        for price in prices:
            count+=1
            if cur>price:
                break
        answer.append(count)
    return answer
