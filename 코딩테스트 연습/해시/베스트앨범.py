def solution(genres, plays):
    answer = []
    sum_of_genre = {gen : 0 for gen in set(genres)}
    for idx in range(len(plays)):
        sum_of_genre[genres[idx]]+=plays[idx]
    
    priority = [gen for gen in set(genres)]
    priority.sort(key = lambda x : -sum_of_genre[x])
    
    music = {gen :[] for gen in set(genres)}
    for idx in range(len(plays)):
        music[genres[idx]].append([idx,plays[idx]])
    for gen in music.keys():
        music[gen].sort(key = lambda x : (-x[1],x[0]))
    
    for gen in priority:
        if len(music[gen])<2:
            answer.append(music[gen][0][0])
        else:
           for i in range(2):
                answer.append(music[gen][i][0])
                
        
    return answer
