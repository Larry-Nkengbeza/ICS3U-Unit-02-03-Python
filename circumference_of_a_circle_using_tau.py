# Created by Larry Nkengbeza
# Created in November 2020
# This program calculates circumference of a circle using tau

import constants


def main():
    # This function calculates circumference
    # Input
    radius = int(input("Enter radius of the circle(mm): "))

    # Process
    Circumference = constants.Tau*radius

    # Output
    print("")
    print("Circumference is {}mm²".format(Circumference))


if __name__ == "__main__":
    main()
