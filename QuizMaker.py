import csv
import os
import time

question_list = [[]]

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

    # run_quiz("testQuiz")
    global question_list
    question_list = [["How many teams are there in the NHL?", "16", "31", "32", "28", "2"],
                     ["How many Stanley Cups did Wayne Gretzky win in his career?", "4", "6", "3", "5", "0"]]
    is_user_finished()


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
        for line in csv_reader:  # Loops through all the questions in the quiz
            print(line["question"])
            for i in questions_numbers:  # Prints out the answers to the question -- there's probably a better way to do this than string concatonation, but this is good for now
                answer_to_print = "answer_" + str(i)
                print("(" + str(i) + ") " + line[answer_to_print])
            print("Which answer do you think is correct? (Answer with the corresponding number of the question)")
            user_guess = input()
            if str(int(user_guess) - 1) == line["index_of_correct_answer"]:  # Checks if the user's guess is correct
                print("Nice Job, you got it right!")
                total_answers_count += 1
                correct_answers_count += 1
                time.sleep(0.25)
                print("\n")

            else:
                correct_answer = line["answer_" + str(int(line["index_of_correct_answer"]) + 1)]
                print("Aw rats. The correct answer was " + correct_answer + ". You guessed " + line[
                    "answer_" + user_guess])  # Prints the correct answer if the user got the question wrong
                total_answers_count += 1
                time.sleep(0.25)
                print("\n")

        print("Your final score was " + str(correct_answers_count) + " out of " + str(
            total_answers_count) + " total questions.\nGiving you a percentage of " + str(
            round(correct_answers_count / total_answers_count,
                  4) * 100))  # Gives the user their final score and percentage


def create_quiz():
    global question_list
    print("What would you like to name your new quiz?")
    quiz_name = input()
    user_is_finished = False
    question_list = [[]]
    while not user_is_finished:
        question_list.append(create_question())
        user_is_finished = is_user_finished()

    current_work_dir = os.getcwd()
    quiz_folder = os.listdir(current_work_dir + "/Quizzes")
    with open(str(quiz_folder) + "/" + quiz_name + ".csv", "w", newline="") as new_quiz:
        writer = csv.writer(new_quiz)
        writer.writerow(["question", "answer_1", "answer_2", "answer_3", "answer_4", "index_of_correct_answer"])
        writer.writerows(question_list)


def is_user_finished():
    # This function asks the user if they are finished creating their quiz, or if they would like to edit one of
    # their questions. If they choose to edit, they will be able to choose one of their questions to edit and then
    # they will be asked again if they want to create another question. The function returns a boolean value of false
    # if the user wishes to create a new question and a value of true if they do not.
    global question_list
    user_choice = input(
        "\nWould you like to create another question? Enter Yes if you would, enter No if you are finished, and enter Edit if you want to Edit one of your questions.\n")
    user_is_finished_method_return = False
    if str.lower(user_choice) == "yes":
        user_is_finished_method_return = False
    elif str.lower(user_choice) == "no":
        user_is_finished_method_return = True
    elif str.lower(user_choice) == "edit":
        print("Which question would you like to edit?")
        counter = 0
        for question in question_list:
            counter += 1
            print("(" + str(counter) + ")" + str(question))
        print("Select the number corresponding to the question you want to edit (make sure to enter a number)")
        user_choice = input()
        question_list.append(edit_question(question_list[int(user_choice) - 1]))
    else:
        print("Please enter 'Yes', 'No', or 'Edit'\n")
        is_user_finished()

    return user_is_finished_method_return


def create_question():
    question = [input("What the question you would like to ask?\n"), input("What is the first option?\n"),
                input("What is the second option?\n"), input("What is the third option?\n"),
                input("What is the fourth option?\n")]
    index_of_correct_answer = input("Which answer is the correct one (please input a number between 1-4 inclusive)\n")
    if validate_index_of_correct_answer(index_of_correct_answer):
        question.append(str(int(index_of_correct_answer) - 1))
    print("The question you just created has the following values: ")
    print("Question: " + question[0])
    print("First option: " + question[1])
    print("Second option: " + question[2])
    print("Third option: " + question[3])
    print("Fourth option: " + question[4])
    print("And the correct option is option " + str(int(question[5]) + 1))
    return question


def edit_question(question):  # This function allows for the editing of single questions
    # Prints the menu
    print("Which element of the question would you like to edit?")
    print("(1)Question: " + question[0])
    print("(2)First option: " + question[1])
    print("(3)Second option: " + question[2])
    print("(4)Third option: " + question[3])
    print("(5)Fourth option: " + question[4])
    print("(6)Correct option" + question[5])
    print("Please input the number corresponding to the option you wish to edit")
    user_choice = input()
    if user_choice == "1":
        question[0] = input("What would you like this to say?")
    elif user_choice == "2":
        question[1] = input("What would you like this to say?")
    elif user_choice == "3":
        question[2] = input("What would you like this to say?")
    elif user_choice == "4":
        question[3] = input("What would you like this to say?")
    elif user_choice == "5":
        question[4] = input("What would you like this to say?")
    elif user_choice == "6":
        question[5] = input("What would you like this to say?")
    return question

def validate_index_of_correct_answer(index_of_correct_answer):
    if int(index_of_correct_answer) >= 1 or int(index_of_correct_answer) <= 4:
        return True
    else:
        return False


def menu():
    print("Welcome to the Quizzinator application!\nOptions:\n(1)Start a quiz\n(2)Create a quiz\n(3)Import a quiz\n"
          "(4)Exit the program")
    user_choice = input()

    if user_choice == "1":
        print("starting quiz")
        # Make this start the quiz
        open_quiz()
    elif user_choice == "2":
        print("Opening the quiz creator")
        # make this open the quiz creator
        create_quiz()
    elif user_choice == "3":
        print("Opening the quiz importer")
        # import_csv() (It don't work lol)
    elif user_choice == "4":
        print("Exiting the program. Goodbye.")
    elif user_choice == "debug":
        print("Time for testing!")
        testing()
    else:
        print("Invalid Input - please try again (to select an option, input the number beside it.")
        menu()


menu()
