def pow(x, y) :
   """eleve x a la puissance y"""
   if y == 0:
       return 1
   else:
       return pow(x,y-1)*x

print(pow(42, 0)) # 1
print(pow(1, 10)) # 1
print(pow(2, 5)) # 32
print(pow(7, 2)) # 49
