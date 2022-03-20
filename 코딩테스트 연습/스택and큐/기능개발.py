def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    
    while progresses:
        num = 0
        while(progresses and progresses[-1]>=100):
            num+=1
            progresses.pop()
            speeds.pop()
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        if num!=0:
            answer.append(num)
            num=0
    return answer
