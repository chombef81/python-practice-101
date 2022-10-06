marks = {"Maths": 80,
"science": 82,
"technology": 35,
"support": 70,
"development": 90,
}

# print dictionary of marks
print(f"Marks: {marks}")

# print keys of dictionary
for subject in marks.keys():
    print(f"subject: {subject}")

# print values of dictionary
for score in marks.values():
    print(f"score: {score}")

# print key and values of dictionary
for subject, score in marks.items():
    print(f"subject: {subject}")
    print(f"score: {score}")

# print values that are less than 50
for subject, score in marks.items():
    if score <= 50:
        print(f"failed: {subject}")
    else:
        print(f"passed: {subject}")

# update lowest value to new value
marks["technology"] = 70
print(f"new score in technology: {marks['technology']}")

# adding new key and value to dictionary
marks["geography"] = 78
for subject, score in marks.items():
    if score <= 50:
        print(f"failed: {subject}")
    else:
        print(f"passed: {subject}")

# deleting old key and value from dictionary
del marks["support"]