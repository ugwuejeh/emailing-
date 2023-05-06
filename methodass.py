# We created a class that adds, debits and deletes itself
class Bankaccount:
     
     balance = 0
     funds1= 0
     funds2= 0
     withdrawal = 0
     

    # we created a method that add funds
     def add(self):
        Total_funds = self.funds1 + self.funds2
        return Total_funds
    
    # we created a method that debits funds
     def debit(self):
         Final_bal = self.balance - self.withdrawal
         if self.balance >= self.withdrawal: 
             return Final_bal
         else:
             return "Insufficient funds"
         
        
    # we created a method that deletes itself
     def deletion(self):
         del Bankaccount.add
         return "Method deleted"
         

# We created the object of the class
check_funds = Bankaccount()

# We assigned instances to the objects
check_funds.balance= 1000
check_funds.funds1= 200
check_funds.funds2= 400
check_funds.withdrawal= 210

# we called the functions
print(check_funds.add())
print(check_funds.debit())
print(check_funds.deletion())