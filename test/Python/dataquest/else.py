#!/usr/bin/env python
# The code in an else statement will be executed if the if statement boolean is False.
# This will print "Not 7!"
a = 6
# a doesn't equal 7, so this is False.
if a == 7:
    print(a)
else:
    print("Not 7!")

# This will print "Nintendo is the best!"
video_game = "Mario"
# video_game is "Mario", so this is True
if video_game == "Mario":
    print("Nintendo is the best!")
else:
    print("Sony is the best!")

season = "Spring"

# Write an if statement that prints "It's hot!" 
# when the season is "Summer" Add an else statement 
# to the if that prints "It might be hot!".
if season == "Summer":
    print("It's hot!")
else:
    print("It might be hot!")