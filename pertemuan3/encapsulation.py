# Python Encapsulation

# Private Properties

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age  # Private property

p1 = Person("Emil", 25)
print(p1.name)
# print(p1.__age)  # This will cause an error


# Get Private Property Value (Getter)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p2 = Person("Tobias", 25)
print(p2.get_age())


# Set Private Property Value (Setter with Validation)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p3 = Person("Linus", 30)
print(p3.get_age())

p3.set_age(31)
print(p3.get_age())


# Example: Encapsulation with Validation

class Student:
  def __init__(self, name):
    self.name = name
    self.__grade = 0

  def set_grade(self, grade):
    if 0 <= grade <= 100:
      self.__grade = grade
    else:
      print("Grade must be between 0 and 100")

  def get_grade(self):
    return self.__grade

  def get_status(self):
    if self.__grade >= 60:
      return "Passed"
    else:
      return "Failed"

student = Student("Adit")
student.set_grade(85)
print(student.get_grade())
print(student.get_status())


# Protected Properties (Convention with Single Underscore)

class Employee:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary  # Protected property (convention)

e1 = Employee("Budi", 50000)
print(e1.name)
print(e1._salary)  # Can access, but not recommended


# Private Methods

class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    return isinstance(num, (int, float))

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
# calc.__validate(5)  # This will cause an error


# Name Mangling

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p4 = Person("Emil", 30)


print(p4._Person__age)