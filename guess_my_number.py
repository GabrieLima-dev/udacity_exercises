import random
answer = random.randint(1, 10)
guess = int(
    input('What value do you think is the real? \nEnter values between 1 and 10.? \n'))

if guess > 10:
    result = "Oh no, you entered an incorrect number. \nEnter a number between 1 and 10."
else:
    if guess < answer:
        result = "Oops! Your guess was too low. \nThe number thought was: {}".format(
        answer)
    elif guess > answer:
        result = "Oops! Your guess was too high. \nThe number thought was: {}".format(
        answer)
    elif guess == answer:
        result = "Nice! Your guess matched the answer!"

print(result)
