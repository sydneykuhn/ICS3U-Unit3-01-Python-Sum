#!/usr/bin/env python3

# Created by: Sydney Kuhn
# Created on: Sep 2020
# This program calculates the sum of two numbers
#    provided by user


def main():

    # this function calculates the sum

    # input
    first = int(input("Enter First Number (Integer): "))
    second = int(input("Enter Second Number (Integer): "))

    # process
    sum = first + second

    # output
    print("")
    print("{0} + {1} = {2}".format(first, second, sum))


if __name__ == "__main__":
    main()
