#Data Type

#1.String
print("Hello"[4])
street_name = "Abbey Road"
print(street_name[4] + street_name[7])

#type conversion
num_char = len(input("what is your name? "))
new_num_char = str(num_char)
print("Ypur name has " + new_num_char +" "+"characters.")

#if we put the no in doble inverted comma it will not count as a number it will just count as an another text
print("123" + "345") 
#the above e.g will not add it as mathimatically. it will just conacatenate like we have seen in day1 e.g of hello + world
print(str(70) + str(101))


#2.Integers
print(123 + 345)

print(123_456_789)
#for human understanding the undercore is used in python for the large number like in real world we use comma so in pyhton we use(_)

#3.Float --- It is nothing but decimal point
a=(3.14159)
print(type(a))

#Boolean --- It is nothing but True & False
True
False