import random

def main():
    score = get_valid_score()
    choice = ''
    while choice != 'Q':
        print_menu()
        choice = input("Enter your choice: ").upper()

        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            result = get_score_result(score)
            print(f"Result: {result}")
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Goodbye!")
        else:
            print("Invalid choice, please try again.")

def print_menu():
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")

def get_valid_score():
    score = int(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score, please enter a score between 0 and 100.")
        score = int(input("Enter a valid score (0-100): "))
    return score

def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    elif score >= 0:
        return "Bad"

def show_stars(score):
    print('*' * score)

main()