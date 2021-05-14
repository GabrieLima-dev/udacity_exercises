state = 'CA', 'MN', 'NY'
question_state = input("What's your status? \n(CA, MN, NY) \n")
purchase_amount = float(input("Purchase amount: "))

if question_state == state[0]:
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state[0], total_cost)

elif question_state == state[1]:
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state[1], total_cost)

elif question_state == state[2]:
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(
        state[2], total_cost)

print(result)
