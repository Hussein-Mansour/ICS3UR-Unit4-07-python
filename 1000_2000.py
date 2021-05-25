#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Sat/May15/2021
# This program prints the integers from 1000 to 2000
# with five integers per line


def main():
    # this function uses one for loop and one if statement
    # process  & output
    for year in range(1001, 2000 + 2):
        if year % 5 == 0:
            print(year - 1)
        else:
            print(year - 1, end="\t")


if __name__ == "__main__":
    main()
