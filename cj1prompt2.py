#Write a python program that prints:
#the sum of two floating point numbers
#the difference between two integers
#the product of a floating point number and an integer
#in each case, print the data type of the answer
#main function
def main():
	#initialize variables
	float_one = 38.0
	float_two = 22.0
	#set variable to result
	sum = float_one + float_two
	#print result along with data type
	print("Sum of floats:", sum, "type:", type(sum))
	integer_one = 41
	integer_two = 19
	diff = integer_one - integer_two
	print("Difference of integers:", diff, "type:", type(diff))
	product = float_one * integer_two
	print("Product of float and integer:", product, "type:", type(product))

if __name__ == '__main__':
	main()