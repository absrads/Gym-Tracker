reg_exercises = {
    "cp": "chest_press.txt",
    "sp": "shoulder_press.txt",
    "row": "row.txt",
    "pull": "pull_up.txt"
}

cardio = {
    "treadmill": "treadmill.txt"
}

max_lift = {
    "bench": "bench_press.txt",
    "deadlift": "deadlift.txt"
}

exercise = input("Enter exercise: ")

all_commands = []

for k, v in reg_exercises.items():
    all_commands.append(k)

for k, v in cardio.items():
    all_commands.append(k)

for k, v in max_lift.items():
    all_commands.append(k)

while exercise not in all_commands:
    print("pp poopoo idiot head")
    exercise = input("Enter exercise: ")

if exercise in reg_exercises:
    day = input("Enter day: ").strip()
    month = input("Enter month: ").strip()
    weight = input("Enter weight: ").strip()
    rep_str = input("Enter reps for each set or setsxreps: ").strip()

    rep_chars = list(rep_str)
    if rep_chars.__contains__("x"):
        rep_str = ""
        sets = float(rep_chars[0])
        reps = ""

        i = 2
        while i < len(rep_chars):
            reps += rep_chars[i]
            i += 1

        for i in range(sets):
            rep_str += reps
            rep_str += " "

    open(reg_exercises[exercise], "a").write(
        f"{day} {month} {weight} {rep_str}\n")
