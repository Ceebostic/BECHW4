import random
# list of moods
moods = ["happy", "sad", "energetic", "calm"]
#list of days
days=["monday", "tuesday", "wednesday", "thursday", "friday"]
#loop through
for i in range(len(days)):
    mood=random.choice(moods)
    print(f"On {days[i]}, you were feeling {mood}.")

import random
moods=["happy", "sad", "tired", "excited", "anxious"]
days=  ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times=["morning", "afternoon","evening"]
for day in days:
    for time in times:
        mood=random.choice(moods)
        print(f"On {day} {time} you were {mood}")