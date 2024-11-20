import random
a = int(input())
b = int(input())
if a>b:
    print("First number should be smaller.")
else:
    print(random.randint(a, b))