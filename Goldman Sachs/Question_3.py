def countSubArrayProductLessThanK(a, n, k):
    #Code here
    product = 1
    subarray = 0
    mini = 0
    count = 0
    for i in range(n):
        product = product * a[i]
        subarray += 1
        
        while(product >= k and mini <= i):
            product /= a[mini]
            mini += 1
            subarray -= 1
        
        if(product < k):
            count += subarray
            
    return count

print(countSubArrayProductLessThanK([1, 2, 3, 4,], 4, 10))