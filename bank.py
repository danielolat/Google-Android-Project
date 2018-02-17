class bank:
    
    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self, amount):
        self.balance=self.balance - amount
    
    def deposit(self, amount):
        self.balance=self.balance + amount
   
    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance)

class process(Account):
    def __init__(self, filepath):
        Account.__init__(self, filepath)
        
    def transfer(self, amount):
        self.balance=self.balance - amount

        process=process("account\\balance.txt")
        process.transfer(100)
        print(process.balance)
        process.commit
    
    

