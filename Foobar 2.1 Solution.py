def solution(lis):

    n = len(lis)

    if n == 1:
        return str(lis[0])
    
    max_neg = -1000
    for each in lis:
        if each < 0 and each > max_neg:
            max_neg = each
        
    count_neg = 0
    count_zero = 0
    prod = 1
    
    for i in range(n):

        if lis[i] == 0:
            count_zero += 1
            continue

        if lis[i] < 0:
            count_neg += 1
 
        prod = prod * lis[i]
 
    if count_zero == n:
        return str(0)
 
    if count_neg & 1:
 
        if (count_neg == 1 and count_zero > 0 and
            count_zero + count_neg == n):
            return str(0)
 
        prod = int(prod / max_neg)
 
    return str(prod)