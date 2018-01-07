
def del_chars(string, n):
    j = 0
    sol = ""        
    while n > 0 and j < len(string) - 1 :
        if sol != "" and string[j] > sol[-1] :
            while n > 0 and len(sol) > 0 and string[j] > sol[-1] :          # check previous chars in sol
                sol = sol[:-1]
                n -= 1   
            sol += string[j]
        elif string[j] < string[j+1]:                                       # check next char in string
            n -= 1                              
        elif string[j] == string[j+1]:                                      # check next equal chars in string
            k = j+1
            while k < len(string) and string[k] == string[j]:
                k += 1               
            if k == len(string) or (k < len(string) and string[j] < string[k]):
                while n > 0 and j < k :                                     # delete them all 
                    n -= 1
                    j += 1
                j -= 1
            else:
                sol += string[j]
        else:
            sol += string[j]
        
        # check last added char
        if n > 0 and len(sol) > 1 and sol[-1] > sol[-2]:
            sol = sol[:-1]
            n -= 1  
            
        # continue 
        j += 1 
            

    if n == 0:
        if j < len(string):
            sol += string[j:]                
    elif j == len(string) - 1:
        if string[j] <= sol[-1]:
            n -= 1
        else:
            sol = sol[:-1]
            sol += string[j]
            n -= 1     
            
    return sol, n            

t = int(input().strip())
for i in range(t):
    text, m = input().split()
    m = int(m)
    recheck = True
    while recheck:       
        recheck = False        
        text, m = del_chars(text, m)
        if m != 0:
            recheck = True
    print(text)
