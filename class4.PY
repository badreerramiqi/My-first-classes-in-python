class Mobile():
    def __init__(self, name, companyName, storage, serialNum, dualSim, support4K):
        self.name = name
        self.companyName = companyName
        self.storage = storage
        self.serialNum = serialNum
        self.dualSim = dualSim
        self.support4K = support4K
    
    def info(self):
        print("The {} is produced by {} Company. It has {}GB storage capacity, its serial number is {}, and it {}supports dual SIM functionality. With {} support, it has a 4K display.".format(self.name, self.companyName, self.storage, self.serialNum, self.dualSim, self.support4K))
    
    # The following methods are commented out because they are not implemented in the code
    # def call():
    # def sendMessage():
    # def playMedia():

mobile1 = Mobile("Redmi not 8 pro", "Redmi", 128, 168452795324, "", "not")
mobile2 = Mobile("iPhone 15", "Apple", 256, 657892456327, "not", "")

mobile1.info()
mobile2.info()
