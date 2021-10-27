class Person:
    pass


# setter and getter
person = Person()
key = 'first_name'
value = 'Weiping'
setattr(person, key, value)
print(getattr(person, key))