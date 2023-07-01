# Quiz Game
# Munteanu Mihnea @ Mihnea03

from quiz_brain import Quiz

def main():
    quiz = Quiz()

    nr = 1

    while quiz.ask_question(nr) == True:
        nr += 1

    return

if __name__ == '__main__':
    main()
