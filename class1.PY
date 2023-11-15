class Employer():
    def __init__(self, number, name, sales, bonushrs, basesalary=0):
        # Initialize the Employer object with the provided parameters
        self.number = number
        self.name = name
        self.sales = sales
        self.bonushrs = bonus_hrs
        self.basesalary = base__salary
    
    def info(self):
        # Display information about the employee
        print("The employee number is {}. Name is {}. Base salary is {}. Sales are {}.".format(self.number, self.name, self.base_salary, self.sales))
    
    # The following method is commented out because it's not implemented in the code
    # def calculateNetSalary():


emp1 = Employer(1, "Badre", 20000, 42)
emp2 = Employer(2, "Mouhamed", 1000, 65, 60000)

emp1.info()
emp2.info()
