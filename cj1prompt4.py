#Write a python program that:
#declares a class describing your favorite animal
#have data members:
#arm length(float), leg length(float), number of eyes(int), tail(bool), furry(bool)
#write an initialization function that sets data members of the class
#write a member function of the class to print out and describe the data members

#define the Penguin class
class Penguin:
	#initialization function and initialize self vars
	def __init__(self, arm_length=8.5, leg_length=4.0, eyes = 2, tail = True, furry = False):
		self.arm_length = arm_length
		self.leg_length = leg_length
		self.eyes = eyes
		self.tail = True
		self.furry = False
	#print member function
	def print(self):
		print("The penguin's characteristics:")
		print(f"Arm length: {self.arm_length}")
		print(f"Leg length: {self.leg_length}")
		print(f"Eye count: {self.eyes}")
		print(f"Tail?: {self.tail}")
		print(f"Furry?: {self.furry}")

#define main function
#set var to be a member of the penguin class
def main():
	fav_animal = Penguin()
	fav_animal.print()

if __name__ == '__main__':
	main()
