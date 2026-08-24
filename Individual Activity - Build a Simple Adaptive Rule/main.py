"""
Adaptive Fitness Tracking App - Simple Rule-Based Personalization
CS412 - Activity: Build a Simple Adaptive Rule (Code Version)

This is a small console program that shows how a fitness tracking app
could look at a user's activity patterns and give them helpful, personal
suggestions automatically. It's based on the "Behavior-Based User Model"
idea from Module 1 (Observation -> Representation -> Inference -> Adaptation).

Instead of just checking one simple number, both rules here look at a
pattern over several days. This is closer to how a real fitness app would
actually notice a habit forming (or breaking) instead of just reacting to
one day at a time.

The data below is made up. It is not connected to a real fitness tracker,
it is only there to show how the rules work.
"""

# ---------------------------------------------------------
# STEP 1: Fake "logged" user data (Observation Layer)
# ---------------------------------------------------------
# Each user has:
# - daily_steps: steps for the last 7 days, in order Mon, Tue, Wed, Thu,
#   Fri, Sat, Sun.
# - workout_log: True/False for whether they worked out on that same day,
#   also Mon through Sun, where the last value (Sun) is "today".

users = [
    {
        "name": "James",
        "daily_steps": [9000, 8700, 9300, 8900, 9100, 2000, 1800],
        "workout_log": [True, True, True, True, True, True, True],
    },
    {
        "name": "Jake",
        "daily_steps": [8200, 8100, 8300, 8000, 8400, 8100, 8200],
        "workout_log": [True, True, True, True, True, True, True],
    },
    {
        "name": "Jim",
        "daily_steps": [6000, 6200, 5900, 6100, 6300, 6100, 6000],
        "workout_log": [False, False, True, True, True, True, False],
    },
]

WEEKDAY_INDEXES = [0, 1, 2, 3, 4]   # Mon-Fri
WEEKEND_INDEXES = [5, 6]            # Sat-Sun


# ---------------------------------------------------------
# STEP 2: The adaptive rules (Inference + Adaptation Layer)
# ---------------------------------------------------------

def rule_1_weekend_drop(user):
    """
    Rule 1: If a user's average weekend steps are less than half of their
             average weekday steps -> Then suggest a fun, low-pressure
             "weekend mini challenge" instead of a normal workout reminder.

    Why this rule: Most fitness apps just remind everyone the same way,
    every day. This rule instead looks for a PATTERN across the week: a
    user who is active on weekdays but drops off on weekends is not lazy,
    they probably just have a different routine (no set schedule, family
    time, etc). A generic "go workout" reminder ignores that. A weekend
    mini challenge (like a walk with a friend, or exploring a new route)
    fits their actual lifestyle better and is more likely to be followed.
    """
    messages = []
    weekday_steps = [user["daily_steps"][i] for i in WEEKDAY_INDEXES]
    weekend_steps = [user["daily_steps"][i] for i in WEEKEND_INDEXES]

    avg_weekday = sum(weekday_steps) / len(weekday_steps)
    avg_weekend = sum(weekend_steps) / len(weekend_steps)

    if avg_weekend < (avg_weekday * 0.5):
        messages.append(
            f"Your weekday steps average {avg_weekday:.0f}, but your weekend "
            f"average drops to {avg_weekend:.0f}. Try this weekend mini "
            f"challenge: a 20-minute walk somewhere new with a friend."
        )
    return messages


def rule_2_broken_streak(user):
    """
    Rule 2: If a user had a workout streak of 3 or more days in a row and
             then missed today -> Then send an encouraging "get back on
             track" message with a very short, easy workout, instead of
             treating them like they are starting completely from zero.

    Why this rule: A lot of apps just say "you missed your goal today,"
    which can feel discouraging and makes people give up on the streak
    altogether. This rule specifically checks if they had real momentum
    (3+ days in a row) before the miss. Since they clearly had a habit
    going, the system responds gently, with a small 5-minute workout, to
    make it easy for them to pick the streak back up instead of feeling
    like they failed and have to start over.
    """
    messages = []
    log = user["workout_log"]
    today_missed = not log[-1]

    if today_missed:
        # Count the streak of workout days right before today
        streak = 0
        for day_worked in reversed(log[:-1]):
            if day_worked:
                streak += 1
            else:
                break

        if streak >= 3:
            messages.append(
                f"You missed today, but you had a {streak}-day workout "
                f"streak going. Don't lose it, try this quick 5-minute "
                f"routine to keep your momentum alive."
            )
    return messages


# ---------------------------------------------------------
# STEP 3: Run the rules on each user and show the output
# ---------------------------------------------------------

def build_personalized_feed(user):
    """Combines the output of both rules into one list of messages."""
    messages = []
    messages += rule_1_weekend_drop(user)
    messages += rule_2_broken_streak(user)
    return messages


def main():
    print("=" * 60)
    print(" ADAPTIVE FITNESS DASHBOARD (Demo)")
    print("=" * 60)

    for user in users:
        print(f"\nUser: {user['name']}")
        feed = build_personalized_feed(user)

        if not feed:
            print("  No adaptive suggestions right now - great job!")
        else:
            for i, message in enumerate(feed, start=1):
                print(f"  [Suggestion {i}] {message}")

    print("\n" + "=" * 60)
    print(" End of session.")
    print("=" * 60)


if __name__ == "__main__":
    main()