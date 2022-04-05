import heapq

def solution(operations):
    answer = []
    heap = [] #정렬을 위한 heap
    stack=[] #임시 저장용 stack
    
    for op in operations:
        if op[0]=="I":#입력을 하는 부분
            heapq.heappush(heap,int(op[2:]))#입력과 동시에 정렬
        else:#출력을 하는 부분
            if int(op[2:])==-1 and heap:#최솟값을 출력할때에는 heap이 비어 있지 않는 경우 heapq의 heappop을 사용한다
                heapq.heappop(heap)
            else:#최댓값을 출력할때
                while heap:#heap의 모든원소를 stack으로 옮긴다
                    stack.append(heapq.heappop(heap))
                if stack:#가장 마지막에 pop된 원소가 최댓값이기 때문에 삭제한다
                    stack.pop()
                while(stack):#다시 원래 heap으로 돌려놓는다
                    heapq.heappush(heap,stack.pop())
    if heap:#heap의 원소 개수에따라 출력 형식이 달라진다
        if len(heap)==1:#heap 이 한개인 경우 최소,최대값이 같다
            answer=[int(heap[0]),int(heap[0])]
        else:#힙이 여러개인경우
            answer.append(heapq.heappop(heap))#최소값
            while heap:
                min = heapq.heappop(heap)
            answer.append(min)#최대값
            answer.reverse()#출력형식
    else:#heap이 빈경우
        answer=[0,0]
    return answer
