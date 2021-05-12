import random
answer = random.randint(1, 10)
guess = int(input('What value do you think is the real one?'))

print(answer)

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif guess == answer:
    result = "Nice!  Your guess matched the answer!"

print(result)