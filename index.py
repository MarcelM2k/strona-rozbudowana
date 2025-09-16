
a = 10
b = "xd"
c = True

if not a == 10:
    print(b)
elif a == 132:
    print("XDD")
else:
    print(c) 

for i in range(1, 100 + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)