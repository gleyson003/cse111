

def main():
    introductory_text()

    quest_1 = input("1. I feel that I am a person of worth, at least on an equal plane with others.\n"
                    "Enter D, d, a, or A: ")
    quest_2 = input("2. I feel that I have a number of good qualities.\n"
                    "Enter D, d, a, or A: ")
    quest_3 = input("3. All in all, I am inclined to feel that I am a failure.\n"
                    "Enter D, d, a, or A: ")
    quest_4 = input("4. I am able to do things as well as most other people.\n"
                    "Enter D, d, a, or A: ")
    quest_5 = input("5. I feel I do not have much to be proud of.\n"
                    "Enter D, d, a, or A: ")
    quest_6 = input("6. I take a positive attitude toward myself.\n"
                    "Enter D, d, a, or A: ")
    quest_7 = input("7. On the whole, I am satisfied with myself.\n"
                    "Enter D, d, a, or A: ")
    quest_8 = input("8. I wish I could have more respect for myself.\n"
                    "Enter D, d, a, or A: ")
    quest_9 = input("9. I certainly feel useless at times.\n"
                    "Enter D, d, a, or A: ")
    quest_10 = input("10. At times I think I am no good at all.\n"
                    "Enter D, d, a, or A: ")

    positive_quests = [quest_1, quest_2, quest_4, quest_6, quest_7]
    negative_quests = [quest_3, quest_5, quest_8, quest_9, quest_10]

    total_score = positive_score(positive_quests) + negative_score(negative_quests)

    print(f"\nYour score is {total_score}")
    print("A score below 15 may indicate problematic low self-esteem.")

def introductory_text():
    print("This program is an implementation of the Rosenberg") 
    print("Self-Esteem Scale. This program will show you ten") 
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters: \n")

    print("D means you strongly disagree with the statement.") 
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement. \n")

def positive_score(quests):
    answers_value = {"D": 0, "d": 1, "a": 2, "A": 3}
    score = 0

    for answer in quests:
        point = answers_value[answer]
        score += point
    
    return score

def negative_score(quests):
    answers_value = {"D": 3, "d": 2, "a": 1, "A": 0}
    score = 0

    for answer in quests:
        points = answers_value[answer]
        score += points

    return score

if __name__ == "__main__":
    main()

