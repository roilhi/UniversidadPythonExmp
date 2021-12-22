def MultiplicaNumeros(*nums):
    acc = 1
    for num in nums:
        acc *= num
    return acc

res = MultiplicaNumeros(1,2,3,4)
print(res)