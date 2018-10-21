from collections import namedtuple

Person = namedtuple('Guy','first_name,last_name,email')

p1 = Person('karim','ahmed','k.okasha@gmail.com')
p2 = Person(first_name='Ahmed', last_name='Mohamed',email='')

print(p1)
print(type(p1))
print(p1.first_name)
print(p2)
