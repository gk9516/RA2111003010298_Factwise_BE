def max_score(l, k):
    n = len(l)
    current_sum = sum(l[:k])
    max_sum = current_sum

    for i in range(1, k+1):
        current_sum = current_sum - l[k-i] + l[-i]
        max_sum = max(max_sum, current_sum)

    return max_sum

l=list(map(int,input().split()))
k=int(input())
print(max_score(l,k))
    
        
    
        
