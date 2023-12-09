import time

def calorie_calc():
    print("Welcome to the program")
    age = int(input("Please enter your age: "))
    weight = int(input("Please enter your weight (in kg): "))
    height = int(input("Please enter your height (in cm): "))
    sex = input("Please enter your sex (M/F): ")

    men_bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    women_bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    time.sleep(2)

    activity_levels = [
        ("Little/no exercise", 1.2),
        ("Light exercise", 1.375),
        ("Moderate exercise (3-5 days/wk)", 1.55),
        ("Very active (6-7 days/wk)", 1.725),
        ("Extra active (very active & physical job)", 1.9)
    ]

    sex_bmr = men_bmr if sex.lower() == 'm' else women_bmr

    print("Choose your activity level:")
    for i, (level, _) in enumerate(activity_levels, start=1):
        print(f"{i}. {level}")

    choice = int(input("Enter the corresponding number (1-5): ").strip())

    if 1 <= choice <= 5:
        m_cal = sex_bmr * activity_levels[choice - 1][1]
        print(f"Your maintenance calories are {m_cal}")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

    cut = (m_cal - 300)
    cut_ext = (m_cal - 900)

    bulk = (m_cal + 250)
    bulk_ext = (m_cal + 500)

    print(f"If you are trying to lose weight start at {cut}, but don't go lower than {cut_ext}")
    print(f"If you are trying to gain weight start at {bulk}, but don't go higher than {bulk_ext}")

calorie_calc()
