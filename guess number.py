import random
print("Hello ! What is your name")
name=input()
name=str(name)
print("Well ," + name + ",I am thinking of a number between 1 and 20")
print("You will be given 3 chances to guess it!!")
number = random.randint(1,20)
count=0
while count<3:
    count+=1
    print("Take a guess")
    n=input()
    n=int(n)
    if (n>number):
        print("Your guess is too high")
    if(n<number):
        print("Your guess is too low")
    if(n==number):
        break
if (n==number):
    count = str(count)
    print("Good Job! You guessed my number in " + count + " guesses")
else:
    number=str(number)
    print("You fail , the actual number is " + number)


