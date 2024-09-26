import random
# Task 1: Your Mood Tracker 
    # Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it. Use the random module again to randomly select the mood.

time_of_day = ["morning","afternoon","evening"]

days_of_week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

moods = ["happy","sad","entergetic","calm"]

for day in days_of_week:
    for time in time_of_day:
        mood = random.choice(moods)
        print(f"On {day} {time} you were feeling {mood}.")
        
    print("=" *50)