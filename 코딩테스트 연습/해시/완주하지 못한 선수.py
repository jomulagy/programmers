def solution(participant, completion):
    answer = ''
    n_cpt = {}
    for man in completion:
        n_cpt[man]=0
    for man in completion:
        n_cpt[man]+=1
    for man in participant:
        if n_cpt[man]>0:
            n_cpt[man]-=1
            
        else:
            answer+=man
            break

    return answer


    
