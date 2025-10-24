

attempts = 0
max_attempts = 3
lessons = ["Math", "English", "Biology"]

while attempts < max_attempts:
    print(f"\nAttempt {attempts + 1} of {max_attempts}")
    username = input("What is your Username: ")
    password = input("What is your Password: ")


    if username == "teacher" and password == "12345678":
        for lesson in lessons:
            lesson = input("input grade for student:")
            print(lesson)
        print("Welcome, Teacher!")
        print("Login Successful!")
        break
    elif username == "student" and password == "mypassword":
        print("Welcome, Student!")
        print("You can see your grades here.")
        break
    else:
        print("Unknown username or incorrect password.")
        attempts += 1

        if attempts == max_attempts:
            print("Too many failed attempts. Access denied.")

if username in ["teacher", "student"]:
    lessons = ["Math", "English", "Biology"]
    if username == "teacher":
            input
    print("\nAvailable lessons:")
    for lesson in lessons:
        print("-", lesson)

    chosen_lesson = input("\nChoose your lesson: ").capitalize()

    grades = {
        "Math": "C",
        "English": "A",
        "Biology": "B"
    }

    if chosen_lesson in grades:
        print(f"Your grade in {chosen_lesson} is {grades[chosen_lesson]}")
    else:
        print("Invalid lesson choice.")








       

