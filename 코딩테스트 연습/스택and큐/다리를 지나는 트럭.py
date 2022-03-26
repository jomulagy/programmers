from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    cur_weight = 0
    bridge = deque()
    deq = deque(truck_weights)
    while deq:
        truck = deq.popleft()
        time+=1
        if bridge and len(bridge)>=bridge_length:
            cur_weight-=bridge[bridge_length-1]
        if(weight-cur_weight>=truck):
            bridge.appendleft(truck)
            
            cur_weight+=truck
        else:
            deq.appendleft(truck)
            bridge.appendleft(0)
        
    return time+bridge_length
