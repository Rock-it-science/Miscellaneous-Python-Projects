# imports
import random
import sys
import time
import linecache
# initialize counter for recursion base case
# will incriment on each right answer
# Global so it can be modified in function
global counter
counter = 0


def math():
    # record start time
    start = time.time()
    # for counter less than 10, generate for data for math problems
    for counter in range(10):
        # numbers to add or subtract
        first = random.randint(1, 10)
        second = random.randint(1, 10)
        # generate whether addition or subtraction
        fct_key = random.randint(1, 2)

        # case addition
        if int(fct_key) == 1:
            # generate answer
            add_equation_ans = first + second
            # give question
            print(str(first) + ' + ' + str(second))
            # get answer
            answer = input()
            # check if answer is correct
            if int(answer) == int(add_equation_ans):
                print('correct!')
            else:
                print('nope!')
                # if wrong, give correct answer
                print('The answer was', add_equation_ans)
                break
        # case subtraction (mostly the same as addition case)
        elif int(fct_key) == 2:
            sub_equation_ans = first - second
            print(str(first) + ' - ' + str(second))
            answer = input()
            if int(answer) == int(sub_equation_ans):
                print('correct!')
            else:
                print('nope!')
                print('The answer was', sub_equation_ans)
                break

    # after 10 question have been answered
    if counter == 9:
        print('congratulations!')
        # record end time and subtract start time
        end = time.time() - start
        # print time
        print('You took %.2f' % end, ' seconds to solve 10 questions')
        # add new score to file, will also create new file if it doesn't exist already
        with open("mathGameLeaderboard.txt", "r+") as f:
            f.write('%.2f\n' % end)
        # print top scores (unfortunately they're not ordered yet, but will maybe add that feature later)
        print('top scores: (currently in no particular order)')
        with open("mathGameLeaderboard.txt") as f:
            for line in f:
                sys.stdout.write(line)
    # if you got a question wrong or after you completed all questions:
    print('Try again?')
    yn = input()
    if yn == 'yes':
        # reset counter
        counter = 0
        math()
    elif yn != 'yes':
        sys.exit()
math()
