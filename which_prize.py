points = int(input('What is your score?'))

wooden_rabbit = 50
no_prize = 150
wafer_thin_mint = 180
penguin = 200

if points <= 50:
    print("Congratulations! You won a Wooden Rabbit!")
elif points <= 150:
    print("Oh dear, no prize this time.")
elif points <= 180:
    print("Congratulations! You won a wafer-thin mint!")
else:
    print("Congratulations! You won a Penguin!")
