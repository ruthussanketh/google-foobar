def solution(s):
    lis = list(s)
    n = len(lis)
    for i in range(n):
        if lis[i].islower():
            lis[i] = chr(122 - ord(lis[i]) + 97)
    decoded_string = ''.join([str(elem) for elem in lis])
    return decoded_string

s = input("Enter the string")
print("\nThe decoded string is: " + solution(s))