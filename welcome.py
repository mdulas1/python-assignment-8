class Customer:
  def __init__(self,name,age,gender,house_no,phone_no):
    self.name = name
    self.age = age
    self.gender = gender
    self.house_no = house_no
    self.phone_no = phone_no

  def fullname(self):
    return f"name{self.name}\nage:{self.age}\ngender:{self.gender}\nhouse_no:{self.house_no}\nphone_no:{self.phone_no}"

customer1 = Customer("john moses",20,"male","kampany-phase-1","09034758265")
customer2 = Customer("Tom garba",23,"male","kampany-phase-1","09034758265")
customer3 = Customer("bulus isa",20,"male","kampany-phase-1","09034758265")
customer4 = Customer("jerry mimi",20,"female","sabon-gari-phase-7","09034758265")
customer5 = Customer("abubakar jibrin",22,"male","bauchi","08034758265")
customer6 = Customer("zumunchi yohanna",24,"male","sabon-gari-phase-3","09034758265")
customer7 = Customer("john moses",20,"male","kampany-phase-1","09034758265")
customer8 = Customer("jibrin musa",20,"male","kampany-phase-1","09034758265")
customer9 = Customer("thankgod emmanuel",25,"male","kampany-phase-4","07034758265")
customer10 = Customer("mujahid ahmad",27,"male","halle-phase-7","07004758265")
print(customer3.fullname())