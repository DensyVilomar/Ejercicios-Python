my_dict = {}
with open("zz.txt", "r") as file:
    for lines in file:
        if lines.startswith("From "):
            lines = lines.split()
            email = lines[1]
            if email not in my_dict:
                my_dict[email] = 1
            else:
                my_dict[email] += 1

print(my_dict)

max_messages = None
max_amount = None

for email,amount in my_dict.items():
    if max_amount is None or amount > max_amount:
        max_messages = email
        max_amount = amount

print(f"The person who has more messages is {max_messages} with {max_amount} messages.")