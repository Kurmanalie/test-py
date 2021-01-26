# a = {"1","2","3"}
# b= {'kl','lj'}
# c= {10,11,12}
# a.add("13")
# print(a)
# b.clear()
# print(b)
# print(c)


# numbers = {1, 2, 3}
# numbers.update(i**2 for i in [1, 2, 3])
# print(numbers)

# a = {'key':'value',
# 	'apple':['re','ty']}
# print(a)

# menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
# menu.update({'besh_barmak':130})
# menu.update({'lagman':135})
# menu.pop('borsh')
# print(menu)



# menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
# menu.update({'besh_barmak':130})
# menu.update({'lagman':135})
# menu.pop('borsh')
# print(menu)
# menu.update({'drinks':['Coca-Cola','Sprite','Fanta']})
# print(menu)

# metod1 = {"add","remove","clear","update","difference",
#         "discard","intersection","intersection_update",
#         "pop"}
# medod2 = {"clear","keys","items","get","values","update",
#          "tuple","list","set","dict"}
# metod1.intersection_update(medod2)
# print (metod1)         

# slovo = {}
# i = 1
# while i<=3:
# 	keys = input("keys")
# 	pas = input ("pas")
# 	# print("keys","pas")
# 	i = i + 1
# slovo.update({"keys":"pas"})
# print(slovo)

a_set = set()
i = 0
while i<=10:
	num = int(input ("Введите число"))
	a_set.add(num)
	i += 1
	a_typ = tuple(a_set)
print(a_typ)	


