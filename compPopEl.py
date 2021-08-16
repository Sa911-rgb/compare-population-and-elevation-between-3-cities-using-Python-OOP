# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = input("Enter the first city's name")
city1.country = input("Enter the country's name that city is in")
city1.elevation = input("Enter the city's elevation")
city1.population = input("Enter the city's population")

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = input("Enter the second city's name")
city2.country = input("Enter the country's name that city is in")
city2.elevation = input("Enter the city's elevation")
city2.population = input("Enter the city's population")

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = input("Enter the third city's name")
city3.country = input("Enter the country's name that city is in")
city3.elevation = input("Enter the city's elevation")
city3.population = input("Enter the city's population")

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if (city1.population>=min_population) and (city1.elevation>city2.elevation) and (city1.elevation>city3.elevation):
		return_city = city1
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if (return_city!=city1) and (city2.population>=min_population) and (city2.elevation>city3.elevation):
		return_city = city2
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if (return_city!=city1) and (return_city!=city2) and (city3.population>=min_population):
		return_city = city3

	#Format the return string
	if return_city.name:
		return return_city.name + ", " + return_city.country
	else:
		return ""

print(max_elevation_city(100000)) 
print(max_elevation_city(1000000)) 
print(max_elevation_city(10000000)) 