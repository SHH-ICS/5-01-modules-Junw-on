import random
x = random.randint(1, 100)
y = random.randint(1, 100)
print(f"What is {x} + {y} ?")
inputanswer = int(input())
answer = x + y
if answer == inputanswer:
    print("Correct")
else:
    print("Wrong")