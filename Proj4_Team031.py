# Assignment Title (include Task number if applicable)
# File: ACT_Python_HeaderTemplate_TeamXXX_UCusername.py
# Date:    Day Month Year
# By:      Your Name
# Section: Your Section
# Team:    Your Team Number
#
# ELECTRONIC SIGNATURE
# Type in your name
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This program is a header template that will be used for
# all your python files the rest of the semester.
def find_error(length):
    error_x = .0007 * length ** 2 - .013*length
    error_y = -.0199 * length
    return [error_x, error_y]


shelvingLocations = ["A1", "A2", "C1", "C2", "B1", "B2", "D1", "D2"]
print(
    "This program models the movement of team 31's robot in a hypothetical facility as specified in project 5's RFP.\n"
    "This model is for the robot starting on point A and is based on test data last updated on 3/8/2022. \n"
    "The model models the robot going to a spot in front of the box, the real robot position will change with the "
    "placement of the arm \n"
    "The data used to produce this model, logic behind the model, and graphs can be found in the engineering notebook")
print()
ShelvingString = ""
currentX = 6
currentY = -6
while (not ShelvingString in shelvingLocations):
    ShelvingString = input("Enter shelf the robot should go to ex: A1\n")
ShelvingIndex = shelvingLocations.index(ShelvingString)

boxIndex = 20
while (boxIndex > 12):
    boxIndex = int(input("Enter the number of the box ie a number between 1 and 12\n"))
boxIndex = boxIndex - 1
targetY = (ShelvingIndex % 4) * 24 + 6 + (int(boxIndex / 6)) * 24
moveLength = (targetY - currentY)
error = find_error(moveLength)
theoretial_x = currentX
theoretial_y = targetY
currentX = currentX + error[0]
currentY = currentY + moveLength + error[1]
print("To go to shelf {0} and box {1} the robot will move forward {2}\" and according to the model the robot will"
      "actually be at: \nx = {3:.2f}\"\ny = {4:.2f}\"".format(ShelvingString, boxIndex, moveLength, currentX, currentY))

print()
print("The robot will then turn 90 degrees clockwise which according to the model will have aproximatly 0 error\n")
targetX = 2 + 6 + (boxIndex % 6 + 1) * 6.4 + (int(ShelvingIndex / 4) * 48)
moveLength = (targetX - theoretial_x)
# since we turn 90 degrees the error in the x direction will become the error in the y direction and vice versa
error = find_error(moveLength)
currentX = currentX + moveLength + error[1]
currentY = currentY + error[0]
print("The robot will then move forward {0:.2f}\" in the x direction and according to the model the robot will"
      "actually be at: \nx = {1:.2f}\"\ny = {2:.2f}\"\nTherefore the total error will be:\nx error = {3:.2f}\"\ny error "
      "= {4:.2f}\"".format(moveLength, currentX, currentY,(currentX-targetX),(currentY-targetY)))
