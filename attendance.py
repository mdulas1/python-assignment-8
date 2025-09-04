"""
TASK: Create an AttendanceRegister class.

Requirements:
1. The class should allow marking a student as present or absent.
2. Store attendance records in a dictionary where the student's name is the key.
3. Provide a method to check if a student was present or absent.
4. Provide a method to display the full register.

Example Usage:
    register = AttendanceRegister()
    register.mark_present("John")
    register.mark_absent("Mary")
    print(register.get_status("John"))   # "Present"
    print(register.show_register())      # {"John": "Present", "Mary": "Absent"}
"""
class AttendanceRegister:
  def __init__(self,):
    self.attendances = {}


  def add_students(self,name):
    self.attendances[name] = {}
    if name not in self.attendances:
      self.attendances[name] = "Absent"
      print(f"{name} has been added to the rigister")
    else:
      print(f"{name} already in the regiter")

  

  def mark_present(self,name):
    if name in self.attendances:
      self.attendances[name] = "present"
      print(f"{name} mark as present")
    else:
      print(f"{name} not in register")

  def mark_absent(self,name):
    if name in self.attendances:
      self.attendances[name] = "Absent"
      print(f"{name} marked as absent")
    else:
      print(f"{name} not in register")


  def check_student(self,name):
    if name in self.attendances:
      print(f"{self.attendances[name]} is our student")
    else:
      print(f"{name} not our student")
  

  def show_register(self):
    for student, sign in self.attendances.items():
      print(f"{student} {sign}")
  
register = AttendanceRegister()

register.add_students("jibrin")
register.add_students("ummisalma")
register.add_students("john blus")

register.mark_present("ummisalma")
register.mark_absent("john blus")
register.mark_present("jibrin")

register.check_student("isa")
