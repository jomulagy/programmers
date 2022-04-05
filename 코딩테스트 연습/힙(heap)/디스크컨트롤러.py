import heapq
def solution(jobs):
    answer = 0
    num = len(jobs)
    heapq.heapify(jobs)
    time = 0
    
    while jobs:
        tmp = []
        job = heapq.heappop(jobs)
        while(job[0]>time):
            time+=1
        while jobs:
            cmp = heapq.heappop(jobs)
            if cmp[0]<=time and cmp[1]<job[1]:
                heapq.heappush(tmp,job)
                job = cmp
            else:
                heapq.heappush(tmp,cmp)
        while tmp:
            heapq.heappush(jobs,heapq.heappop(tmp))
            
        
        answer+=(job[1]+time-job[0])
        time+=job[1]
        
    answer//=num
    return answer
