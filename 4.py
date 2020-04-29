def listSum(x) :
   """somme la liste d'elt"""
   if 0 == len(x):
       return 0
   else:
       return listSum(x[1:])+int(x[0])


print(listSum([])) # 0
print(listSum([42])) # 42
print(listSum([3,1,5,2])) # 11
