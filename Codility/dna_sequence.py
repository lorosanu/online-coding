def solution(S, P, Q):
    N = len(S)
    M = len(P)

    impact = {'A' : 1, 'C' : 2, 'G' : 3, 'T' : 4}

    counter = {'A' : 0, 'C' : 0, 'G' : 0, 'T' : 0}
    counters = []        
    counters.append(dict(counter))
    
    for i in range(N):
        counter[S[i]] += 1
        counters.append(dict(counter))

    print("Counters:")
    for k, c in enumerate(counters):
        print(k, "=>", c)
    
    min_impact = []
    for i in range(M):
        x = P[i]
        y = Q[i] + 1
        
        if counters[y]['A'] - counters[x]['A'] > 0:                 # if counter was changed in count of 'A'
            min_impact.append(impact['A'])                    
        elif counters[y]['C'] - counters[x]['C'] > 0:               # if counter was changed in count of 'C'
            min_impact.append(impact['C'])
        elif counters[y]['G'] - counters[x]['G'] > 0:               # if counter was changed in count of 'G'
            min_impact.append(impact['G'])
        else:                                                       # if counter was changed in count of 'T'
            min_impact.append(impact['T'])
            
        print(P[i], Q[i], "=>", x, y, "=>", min_impact[-1])
    return min_impact


print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
print(solution('AACC', [0, 0, 0, 1, 1, 2, 3], [0, 1, 2, 2, 3, 3, 3]))
