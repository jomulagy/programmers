from collections import deque
def search(dq, num):
    for i in dq:
        if num<i[1]:
            return True
    return False

def solution(priorities, location):
    answer = 0
    dq = deque([(i,priorities[i]) for i in range(len(priorities))])
        
    while dq:
        num = dq.popleft()
        
        if dq and search(dq,num[1]):
            dq.append(num)
        else:
            answer+=1
            
            if num[0]==location:
                return answer
