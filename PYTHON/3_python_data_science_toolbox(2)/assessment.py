# Class
#%%
# Using class
class Planet:
    def __init__(self,name):
        self.name = name

m = Planet('mercury')
print(m.name)

#%%
class AstroBody:
    description = 'Natural entity in the observable universe.'

class Star(AstroBody):
    pass

sun = Star()
sun.description

#%%
class Planet:
    def __init__(self,name, diameter_km):
        self.name = name
        self.diameter_km = diameter_km

e = Planet('Earth', 12742)
e.name, e.diameter_km

#%%
class Dog:
    def __init__(self):
        pass

    def bark(self):
        return "bark bark bark ..."

d = Dog()
d.bark()

# Use code for 1 line
# %%
x = ("rose", "sunflower", "daisy")
print(type(x))

#%%
g = lambda x,y: x + y

g(2,3)

# %%
# Decorate the adder() and subtractor function so that the result of the 
# adder function is multiplied by 2 and the result of the subtract function
# is multiplied by 3

def multiply(by = None):
    def multiply_real_decorator(function):
        def wrapper(*args,**kwargs):
            return by * function(*args,**kwargs)
        return wrapper
    return multiply_real_decorator

@multiply(by= 2)
def adder(a,b):
    return a + b

@multiply(by = 3)
def subtractor(a,b):
    return a - b

print(adder(2,3))
print(subtractor(2,3))


# %%
# Access the docstrings of the function

def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)

factorial(3)
factorial.__doc__

# Access to the type of data
# %%
# return the output as {}

x = (1,2,3)
y = list(x)
z = set(x)
print(y)
print(z)
print(type(z))

# %%
# Add 'Gloomhaven' to the boardgames list in the first position
boardgames = [
  'Pandemic Legacy: Season 1', 
  'Terraforming Mars', 
  'Brass: Birmingham'
]
# add to
boardgames.insert(0,'Gloomhaven')
print(boardgames)
print(type(boardgames))

#%%
# Add item to the dictionary -> format:paperback
book = {
    'title': 'The Giver',
    'author': 'Lois Lowry',
    'rating': 4.13
}
book['format'] = 'paperback'
print(book)

#%%
letters = ['a', 'b', 'c']
for ii, x in enumerate(letters):
    print(ii,":",x)

# %%
for i in 'hello':
    if i == 'l':
        continue
    print(i)

# %%
def add_many(*args):
    s = 0
    for n in args:
        s += n
    print(s)

add_many(1,2,3)
# %%
# Upper for list ['hello','world'] 
[s.upper() for s in ['hello','world']]

# %%
# change value of a list 
python_pkgs = ['dplyr', 'pandas', 'scipy']

# change value of the first list to 'numpy'
python_pkgs[0] = 'numpy'
print(python_pkgs)
# %%
