'''
The code is for a trivia game implementation where players take turns answering questions to earn points. The game is played in rounds, and each round consists of two questions, one for each player. The questions are obtained by calling the get_questions() function from the trivia.py module. The players enter their answers by inputting a number between 1 and 4. If the answer is correct, the player earns a point, and the game moves on to the next question. At the end of the game, the player with the most points is declared the winner. If there is a tie, the game declares it as such.
'''

from trivia import get_questions

def play_game():
    questions = get_questions()
    player1_points = 0
    player2_points = 0
    num_questions = len(questions)
    num_rounds = num_questions // 2

    for round in range(num_rounds):
        print("Round", round+1)
        print("---------")

        for i in range(2):
            player = i + 1
            question_num = round * 2 + i
            print(f"Question for the player {player}:")
            print(questions[question_num])
            answer = int(input("Enter your solution (a number between 1 and 4): "))

            if answer == questions[question_num].correct_answer:
                print("That is the correct answer.")
                if player == 1:
                    player1_points += 1
                else:
                    player2_points += 1
            else:
                print(f"That is incorrect. The correct answer is {questions[question_num].correct_answer}")

            print()

    print("Final scores:")
    print(f"Player 1: {player1_points} points")
    print(f"Player 2: {player2_points} points")
    if player1_points > player2_points:
        print("Player 1 wins!")
    elif player2_points > player1_points:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == '__main__':
    play_game()