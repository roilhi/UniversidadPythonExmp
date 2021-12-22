def SumarNumeros(*nums):
    count = 0
    for num in nums:
        count+=num
    return count

# Probando la función
res = SumarNumeros(1,2,3)
print(res)