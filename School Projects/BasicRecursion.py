#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():

    count = 0
    user_number = 0

    user_number = int(input('Please Enter a Number for us to Count:  '))
    recurse_count(count, user_number)


def recurse_count(count, user_number):

    if count < user_number:
        count = (count + 1)
        print (count) 
        return recurse_count(count, user_number)
    else:
        pass


if __name__ == "__main__":
    main()
    print()
    
        


