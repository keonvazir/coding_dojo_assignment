x = "Hello World"
print(x)
y = 42
print(y)

name = "Zen"
print("my name is", name)

name = "Zen"
print("my name is " + name)

first_name = "Keon"
last_name = "Vazir"
age = 26
print(f"my name is {first_name} {last_name} and I am {age} years old.")

first_name = "Keon"
last_name = "Vazir"
age = 26
print("my name is {} {} and I am {} years old.".format(first_name, last_name, age))

hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

x = "hello world"
print(x.title())
# output:
"Hello World"

fave_food1 = "sushi"
fave_food2 = "pizza"
print("my favorite food is {} and my second favorite is {}".format(fave_food1, fave_food2))

fave_food1 = "sushi"
fave_food2 = "pizza"
print(f"my favorite food is {fave_food1} and my second favorite is {fave_food2}")
for x in range(10):
    print(x)

my_list = ["abc", 123, "xyz"]
for v in my_list:
    print(v)

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
    #output = name, language

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k]) 
    # output = Noelle, Python

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("final statement")

for val in "string":
    if val == "i":
        break
    print(val)

for z in range(5, 1000, 1):
    if z%5 == 0:
        print(val)

for x in range(1, 100, 1):
    if x%5 == 0:
        print("coding")
    elif x%10 == 0:
        print("coding dojo")

for x in range(0, 1000, 1):
    sum = 0
    if x%2 == 1:
            sum = sum + x
            print(sum)

# //you get a completly different answer if you put sum = 0 above the for loop

def addOddNumbers(numbers):
    total = 0
    for num in numbers(0, 100, 1):
        if num%2 == 1:
            total = total + num
            print(total)

for num in range(2018, 0, -4):
    print (num)

lowNum=2
highNum=9
mult=3
for num in range(0, 10, 1):
    if num%3 == 0:
            print(num)

def multiple_of_three():
    for i in range(-300, 1):
        if i % 3 == 0 and i != lowNum and i != highNum:
            print (i) 

            #1
def a():
    return 5
print(a())
