import random
n=random.randrange(1,10)
score=10
while True:
    a=int(input("enter your guess"))
    if a==n:
        print("correct guess, you win")
        break
    elif a<n:
        print("too small")
    else:
        print("too large")
    score=score-1
print(score)




