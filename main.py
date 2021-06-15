'''
Higher or lower game. Guess which personality has more instagram followers.
'''
from art import logo, vs
from game_data import data
import random

game_on = True
program_on = True

while program_on:
    score = 0
    print(logo)

    while game_on:
        profile_a = random.choice(data)
        profile_b = random.choice(data)

        while profile_a == profile_b:
            profile_b = random.choice(data)

        print(f"Compare: {profile_a['name']}, a {profile_a['description']}, from {profile_a['country']}")
        print(vs)
        print(f"Against: {profile_b['name']}, a {profile_b['description']}, from {profile_b['country']}")

        choice = input("Who has more followers? Type A or B: ").lower()
        while True:
            if choice == 'a':
                if profile_a['follower_count'] > profile_b['follower_count']:
                    score += 1
                    print('-----------------')
                    print("Correct answer! Score: {}".format(score))
                    break
                elif profile_a['follower_count'] < profile_b['follower_count']:
                    print("Sorry, but that's the incorrect answer!")
                    print(f"{profile_a['name']} has {profile_a['follower_count']}k followers, while {profile_b['name']} has {profile_b['follower_count']}k followers")
                    game_on = False
                    break

            elif choice == 'b':
                if profile_a['follower_count'] < profile_b['follower_count']:
                    score += 1
                    print('-----------------')
                    print("Correct answer! Score: {}".format(score))
                    break
                elif profile_a['follower_count'] > profile_b['follower_count']:
                    print("\nSorry, but that's the incorrect answer!")
                    print(f"{profile_a['name']} has {profile_a['follower_count']}k followers, while {profile_b['name']} has {profile_b['follower_count']}k followers")
                    game_on = False
                    break
            else:
                print("Invalid input! Try again.")
                continue

    while True:
        replay = input(f"Final score: {score}. Want to play again?(y/n): ")

        if replay == 'y':
            game_on = True
            break
        elif replay == 'n':
            program_on = False
            break
        else:
            print("Invalid input. Try again.")
            continue
