import random
num = random.randint(1,100)
guesses = [0]
while True:
    try:
        guess = int(input("Enter a number between 1 & 100 "))
        if guess < 1 or guess > 100:
            print('outside established range')
            continue
        print("You guessed ", guess)
        if guess == num:
            if len(guesses) > 1:
                print("You did it in",len(guesses),'attempts')
            else:
                print("You did it in",len(guesses),"try!\n Great Job!")
            break
        guesses.append(guess)
        if guesses[-2]:
            if abs(num - guess) < abs(num - guesses[-2]):
                print('Warmer!')
            else:
                print('COLDER!')
        else:
            if abs(num - guess) <= 10:
                print("Warm")
            else:
                print('COLD!')
        continue
    except ValueError:
        print("Input a number please")




