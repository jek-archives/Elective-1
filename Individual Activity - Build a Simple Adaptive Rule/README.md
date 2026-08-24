# Adaptive Fitness Tracking App - CS412 Activity

Name: Jake Lloyd P. Quejada
Section: CS4D
Date: August 24, 2026

## About this project

This is a simple console program for a fitness tracking app. It looks at a
user's activity pattern over the past week and gives them personal
suggestions automatically, based on behavior-based user model.

Instead of just checking one number on one day, both rules here look at a
pattern over several days. This is closer to how a real fitness app would
actually notice a habit forming or slipping, instead of reacting to just
one day at a time.

The user data in main.py is made up. It is not connected to a real fitness
tracker, it is only there to show how the rules work.

## How to run it

1. Make sure Python 3 is installed on your computer.
2. Download or clone this repo.
3. Open a terminal in the project folder and run this command:

```bash
python3 main.py
```

No extra installs needed. It will print suggestions for each sample user.

## Rule 1: The Weekend Drop-Off

What Happens: If someone takes less than half their usual weekday steps over the weekend, the system skips the standard workout reminder and suggests a fun, easy activity instead (like a casual walk with a friend).

Why It Works: People have different weekend routines, not a lack of effort. Meeting them where they are feels natural and helpful instead of pushy.

Rule 2: The Streak Recovery

What Happens: If someone works out three days in a row and then misses a day, the system sends a gentle note with a quick 5-minute workout to help them ease back in.

Why It Works: Guilt trip alerts make people give up. Acknowledging their hard work and offering a small step forward keeps their momentum alive.

## Why this helps
Instead of judging a single off day, the system looks at long-term habits. This makes the guidance feel personal, realistic, and encouraging.