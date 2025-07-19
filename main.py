
teachers = [
    {
        "teacher": "Anna",
        "school_class": "10A",
        "ratings": [2, 1, 3] 
    },
    {
        "teacher": "Thomas",
        "school_class": "10A",
        "ratings": [2, 2, 2] 
    },
    {
        "teacher": "Julia",
        "school_class": "10B",
        "ratings": [3, 4, 2] 
    },
    {
        "teacher": "Markus",
        "school_class": "10B",
        "ratings": [1, 2, 2] 
    },
    {
        "teacher": "Sophie",
        "school_class": "10C",
        "ratings": [1, 1, 2] 
    },
    {
        "teacher": "Daniel",
        "school_class": "10C",
        "ratings": [4, 5, 3] 
    },
]

def calc_average_rating(teacher):
    return round((sum(teacher["ratings"]) / len(teacher["ratings"])), 1)

def get_better_teachers(teachers, avg):
    better_teachers = []
    for teacher in teachers:
        avg_rating = calc_average_rating(teacher)
        if avg_rating < avg:
            better_teachers.append( {teacher["teacher"]: avg_rating})
    return better_teachers

def calc_class_average(teachers):
    class_grades = {}

    for teacher in teachers:
        cls = teacher["school_class"]
        if cls not in class_grades:
            class_grades[cls] = []
        class_grades[cls].append(calc_average_rating(teacher))
    
    average_grades = {}
    for school_class, grades in class_grades.items():
        average_grades[school_class] = round(sum(grades) / len(grades), 1)

    return average_grades
        

    

print(get_better_teachers(teachers, 2.5))
print(calc_class_average(teachers))