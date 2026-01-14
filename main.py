# main.py is a simple version of the Fame_fighter game with simple-to-understand code

import random
from art import logo, vs
from game_data import data

print(logo)

a = random.choice(data)
b = random.choice(data)
score = 0


continue_game = False
while not continue_game :
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")

    print(vs)

    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")

    print(a["follower_count"])
    print(b["follower_count"])

    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if a["follower_count"] > b["follower_count"]:
        if user_choice == "a":
            a = b
            b = random.choice(data)
            score += 1
            print("\n" * 20)
            print(f"You're right! Current score: {score}")
        else:
            continue_game = True
            print("\n" * 20)
            print(f"Sorry, that's wrong. Final score: {score}")

    elif a["follower_count"] < b["follower_count"]:
        if user_choice == "b":
            a = b
            b = random.choice(data)
            score += 1
            print("\n" * 20)
            print(f"You're right! Current score: {score}")
        else:
            continue_game = True
            print("\n" * 20)
            print(f"Sorry, that's wrong. Final score: {score}")
    else:
        continue_game = True
        print("\n" * 20)
        print(f"Sorry, that's wrong. Final score: {score}")


