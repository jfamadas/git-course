
def initialize():
	print("Test 1")

def vehicles():
	return ["car", "truck", "bike"]

def main():
	initialize()

	name = "Josep"
	age = 26
	city = "Badalona"
	user = "user2"


	print(name + " is " + str(age) + " years old and lives in " + city + ".")
	print(name + " is user number: " + user)
	print(vehicles())



if __name__ == "__main__":
	main()
