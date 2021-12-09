# Final Project for CS101 Intro to Computing
# Name: John (Jack) Ambery
# Filename: NASAPicOfTheDay.py
#
# Using a program to retrieve data from an API and implements a looping menu
#
# This project is for Introduciton to Computing Final Project

from Picture import Picture

def askForDate():
    print("* NOTE: The date must be on or after June 16, 1995 *")
    day = input("What is the day you would like? (8th = 08, 23rd = 23)\n")
    month = input("What is the month you would like? (March = 03)\n")
    year = input("What is the year you would like?\n")
    return [month, day, year]

#very basic menu
def menu():
    print("Select 1 to open the image online")
    print("Select 2 to see the title image")
    print("Select 3 to see the name of the photographer")
    print("Select 4 to print the full description of the photo") # title, photographer, explanation
    #add option to write the description to a file
    print("Select 0 to quit")

def process():

    picChoice = input("Would you like to use today's image (select '1') or select your own date? (select '2')\n")
    
    if picChoice == '1': # if they want to use today's image
        photo = Picture(0,0,0)
    else: # if they want to choose their own date
        date = askForDate()
        photo = Picture(date[0], date[1], date[2])
    
    while True:

        menu() # displays options of what to do with image

        userSelection = int(input("Please make a selection:\n"))
        if userSelection == 1:
            photo.openImage()
        elif userSelection == 2:
            print(photo.getTitle())
        elif userSelection == 3:
            print(photo.getPhotographer())
        elif userSelection == 4:
            print(photo) # calls repr
        elif userSelection == 0:
            exit()
        else:
            print("invalid selection")


def main():

    process()

if __name__ == "__main__":
    main()

