from datetime import datetime

def check_birthdate(year, month, day):
	birthday = datetime(year,month,day)
	if birthday >=  datetime.now():
		print("Invalid Birthday")
		return False
	calculate_age(year, month, day)
	return True

def calculate_age(year, month, day):
	birthday = datetime(year,month,day)
	current = datetime.today()
	age = current - birthday
	print("You are %s years old" % int(age.days/365))
   

def main():
	year = input("Enter year of birth: ")
	month = input("Enter month of birth: ")
	day = input("Enter day of birth: ")
	check_birthdate(int(year),int(month),int(day))
	



if __name__ == '__main__':
	main()