def hansoo(n):
    cnt = 99
    if n < 100:
        print(n)
        return 0       
    else :        
        for i in range(100, n+1, 1):
            A = i // 100
            B = (i // 10) % 10
            C = i % 10
            
            if (A-B) == (B-C):
                cnt += 1
        print(cnt)
        
n = int(input())
hansoo(n)


