import csv
import os
import time

# TODO: MAKE THIS WORK!
# def import_csv():
#     print("Please enter the directory of the csv file you wish to import: ")
#     csvdir = input()
#     new_name = csvdir.split("\\")[-1]
#
#     with open(csvdir, "r") as csv_file:
#         csv_reader = csv.reader(csv_file)
#
#         with open("Quizzes\\" + new_name, "w") as new_file:
#             csv_writer = csv.writer(new_file)
#
#             for line in csv_reader:
#                 csv_writer.writerow(line)



def testing():
    # This is a function for testing out new functionality
    # fieldnames = ["first_name", "last_name", "email"]
    #
    # print("Please enter the directory of the csv file you wish to open: ")
    # csvdir = input()
    # with open(csvdir, "r") as csv_file:
    #     csv_reader = csv.DictReader(csv_file)
    #
    #     # for line in csv_reader:
    #         # print(line)
    #         # print("line")
    #
    #     new_name = csvdir.split("\\")[-1]
    #
    #     with open("Quizzes\\" + new_name, "w", newline='') as new_file:
    #         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    #
    #         for line in csv_reader:
    #             print(line)
    #             csv_writer.writerows(line)

    run_quiz("testQuiz")


def open_quiz():
    print("Here are the quizzes you currently have")
    currentWorkDir = os.getcwd()
    quizzes_in_quiz_folder = os.listdir(currentWorkDir + "\\Quizzes")
    quizzes_list = []
    for quiz in quizzes_in_quiz_folder:
        current_quiz = quiz.split(".")[0]
        print("current_quiz: " + current_quiz)
        quizzes_list.append(current_quiz)
    print(quizzes_list)

    chosen_quiz = input("Which one would you like to do? ")
    if chosen_quiz in quizzes_list:
        run_quiz(chosen_quiz)
    else:
        print("Invalid entry, please enter the name of a quiz in the quizzes folder")
        open_quiz()


def run_quiz(quiz_name):
    current_work_dir = os.getcwd()
    questions_numbers = [1, 2, 3, 4]
    quiz_location = current_work_dir + "/Quizzes/" + quiz_name + ".csv"
    correct_answers_count = 0
    total_answers_count = 0

    with open(quiz_location, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            print(line["question"])
            for i in questions_numbers:
                answer_to_print = "answer_" + str(i)
                print("(" + str(i) + ") " + line[answer_to_print])
            print("Which answer do you think is correct? (Answer with the corresponding number of the question)")
            user_guess = input()
            if str(int(user_guess) - 1) == line["index_of_correct_answer"]:
                print("Nice Job, you got it right!")
                total_answers_count += 1
                correct_answers_count += 1
                time.sleep(0.25)
                print("\n")

            else:
                correct_answer = line["answer_" + str(int(line["index_of_correct_answer"]) + 1)]
                print("Aw rats. The correct answer was " + correct_answer + ". You guessed " + line["answer_" + user_guess])
                total_answers_count += 1
                time.sleep(0.25)
                print("\n")

        print("Your final score was " + str(correct_answers_count) + " out of " + str(total_answers_count) + " total questions.\nGiving you a percentage of " + str(round(correct_answers_count / total_answers_count, 4) * 100))


def menu():
    print("Welcome to the Quizzinator application!\nOptions:\n(1)Start a quiz\n(2)Create a quiz\n(3)Import a quiz\n"
          "(4)Exit the program")
    userChoice = input()

    if userChoice == "1":
        print("starting quiz")
        # Make this start the quiz
        open_quiz()
    elif userChoice == "2":
        print("Opening the quiz creator")
        # make this open the quiz creator
    elif userChoice == "3":
        print("Opening the quiz importer")
        # import_csv() (It don't work lol)
    elif userChoice == "4":
        print("Exiting the program. Goodbye.")
    elif userChoice == "debug":
        print("Time for testing!")
        testing()
    else:
        print("Invalid Input - please try again (to select an option, input the number beside it.")
        menu()


menu()
