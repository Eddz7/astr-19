#string

s = "I am a string."
print(type(s)) #will say str

#boolean

yes = True #boolean true
print(type(yes))

no = False #boolean false
print(type(no))

#List ordered and changeable

alpha_list = ["a", "b", "c"] #list initialization
print(type(alpha_list)) #will say list
print(type(alpha_list[0])) #will say string
alpha_list.append("d") #will add "d" to list end
print(alpha_list) #will print list

#Tuple ordered and changeable

alpha_tuple = ("a", "b", "c") #tuple initialization
print(type(alpha_tuple)) #will say tuple

try: #attempt the following use
	alpha_tuple[2] = "d" #won't work and will raise TypeError
except TypeError: #when we get a TypeError
	print("We can't add elements to tuple!") #print this message
print(alpha_tuple) #will print tuple