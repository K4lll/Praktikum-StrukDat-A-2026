# Python Inheritance

# Create Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


# Create object from Parent Class
x = Person("John", "Doe")
x.printname()


# Create Child Class (inherit from Person)
class Student(Person):
  pass


# Create object from Child Class
y = Student("Mike", "Olsen")
y.printname()


# Add __init__() Function to Child Class (Override Parent)
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)


z = Student("Anna", "Smith")
z.printname()


# Use super() Function
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)


a = Student("David", "Brown")
a.printname()


# Add New Property
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year


b = Student("Mike", "Olsen", 2019)
b.printname()
print("Graduation Year:", b.graduationyear)


# Add Method in Child Class
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, 
          "to the class of", self.graduationyear)


c = Student("Lisa", "Taylor", 2024)
c.welcome()