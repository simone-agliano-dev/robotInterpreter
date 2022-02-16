# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Robot Interpreter
# You have a robot in a grid-based world. It only knows how to do two things: move forward and turn right.
from abc import abstractmethod


# Your task is to execute a program made of single-character commands. Consider these commands:
# F -> move forward
# R -> turn right
# 1-9 -> repeat the next command n times

# F R F F R F
# robot.move_forward()
# robot.turn_right()
# robot.move_forward()
# robot.move_forward()
# robot.turn_right()
# robot.move_forward()

# F R 2 3 F R F
# robot.move_forward()
# robot.turn_right()
# robot.move_forward()
# robot.move_forward()
# robot.turn_right()
# robot.move_forward()


# scan my program:
#  curr_char = letter or a number
#  if I have a letter and two numbers (x,y) before I will need to run my letter  x*y times going back with the pointer up to another letter
#   otherwise just run the letter interpreter
#
# if curr_char=="F":
#   self.move_forward
# elif curr_char=="R"
#   self.move_right

# for element in iterator:

# 1 F 1 R 1 F 1 F 1 R 1 F
from typing import Iterator


def execute(program: Iterator[str]) -> None:
    number_repeats = 1
    print(program)
    i =0
    for element in program:
        if element.isnumeric():
            number_repeats *= int(element)
        else:
            element = program[i]
            for x in range(number_repeats):
                if element == "F":
                    print("move_forward")

                elif element == "R":
                    print("move right")
            number_repeats = 1
        i+=1


def main():
    execute("FRF23FRF")


if __name__ == "__main__":
    main()
