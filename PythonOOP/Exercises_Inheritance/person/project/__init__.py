

# zero test
from project import Person
from project import Child
import unittest

class Tests(unittest.TestCase):
   def test(self):
      person = Person("Peter", 25)
      child = Child("Peter Junior", 5)
      self.assertEqual(person.name, "Peter")
      self.assertEqual(person.age, 25)
      self.assertEqual(child.__class__.__bases__[0].__name__, "Person")

if __name__ == "__main__":
   unittest.main()


# from child import Child
# from person import Person
#
# person = Person("Peter", 25)
# child = Child("Peter Junior", 5)
# print(person.name)
# print(person.age)
# print(child.__class__.__bases__[0].__name__)