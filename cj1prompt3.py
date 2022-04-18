#Write a python program that:
#defines a function f(x) and returns x**3 + 8
#calls the function with x = 9 and prints the result
#use an if statement that prints "YAY!" if the result is more than 27

#define function f(x) that takes in the argument x
def f(x):
	output = x**3 + 8
	return(output)
#main function that sets a var to the result of f(9) and prints it
def main():
	return_value = f(9)
	print(return_value)
	#if the result is greater than 27, print "YAY!"
	if return_value > 27:
		print("YAY!")
if __name__ == '__main__':
	main()