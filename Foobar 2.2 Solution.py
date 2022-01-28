def solution(s):
    
    n = len(s)
    count = 0;
    
    if n == 1:
        return count
    
    for i in range(n):
        if s[i] == ">":
            for j in range(i,n):
                if s[j] == "<":
                    count = count + 1
                    
    return count*2