
def solution(N):
    binary = "{0:b}".format(N)

    if len(binary) <= 2:
        return 0
    
    max_gap = 0
    last_poz = -1

    i = 0
    while i < len(binary):
        while i < len(binary) and binary[i] == '1':
            last_poz = i
            i += 1

        while i < len(binary) and binary[i] == '0':
            i += 1
   
        if i < len(binary):         
            if last_poz != -1 and binary[i] == '1' :
                if i - last_poz - 1 > max_gap:
                    max_gap = i - last_poz - 1
    return max_gap    
    
N = 1
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 2
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 3
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 4
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 5
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 6
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 7
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 8
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 9
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 15
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 20
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 529
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 1041
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 34634
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 346547654
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))

N = 2147483647
print("N={0}, binary(N)={0:b}, maxgap={1}".format(N, solution(N)))
