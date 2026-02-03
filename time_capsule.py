from datetime import datetime, timedelta

# 1. Setup Dates
today = datetime.now().strftime("%b %d, %Y")
future_date = (datetime.now() + timedelta(days=3650)).strftime("%b %d, %Y")

print("--- 2026 Time Capsule Creator ---")

# 2. Collect Data
age = input("How old are you? ")
song = input("What is your current favorite song? ")
goal = input("What is your biggest goal right now? ")
friend = input("Who is your best friend? ")
feeling = input("In one word, how are you feeling today? ")

# 3. Format the Content
# We use f-strings to create the border and content
header_border = "╔" + "═" * 40 + "╗"
footer_border = "╚" + "═" * 40 + "╝"

content = f"""{header_border}
║           TIME CAPSULE - 2026          ║
║         Created: {today:15}       ║
║      To be opened: {future_date:15}     ║
{footer_border}

> Current Age: {age}
> Favorite Song: {song}
> Biggest Goal: {goal}
> Best Friend: {friend}
> Current Vibe: {feeling}

------------------------------------------
Keep working hard. See you in 10 years!
"""

# 4. Save to File
with open("time_capsule_2026.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("\nSuccess! Your time capsule has been sealed in time_capsule_2026.txt.")