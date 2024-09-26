import random
# Task 1: Your Mood Today 
    # Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through every day of the week and for each day, randomly select a mood from the list and print it. Ensure that your program includes the use of the random module to select the mood.

days_of_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

moods = ["happy","sad","entergetic","calm"]

for day in range(0,len(days_of_week)):
    mood = random.choice(moods)
    print (f"On {days_of_week[day]} you were feeling {mood}.")
