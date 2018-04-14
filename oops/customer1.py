class Customer:
    def __init__(self, rollno, name):
      self.rollno = rollno
      self.name = name
    def search_product(self,product_name):
        print("searching"+product_name)
    def browse_product(self,product_name):
        print("searching"+product_name)
cust1 = Customer("Ajeet","banglor")
cust1.search_product("phone")
print(cust1.name)
