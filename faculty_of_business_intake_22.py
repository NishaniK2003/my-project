# faculty_of_business_intake_22.py

def get_faculty_details():
    details = {
        "Faculty Name": "Faculty of Business",
        "University": "University of Moratuwa",
        "Intake Year": 2022,
        "Programs Offered": [
            "Business Analytics",
            "Financial Services Management",
            "Business Process Management"
        ],
        "Departments": [
            "Department of Decision Sciences",
            "Department of Management of Technology",
            "Department of Industrial Management"
        ],
        "Key Features": [
            "Focus on analytical skill development",
            "Designed for students with quantitative and analytical skills",
            "Open to students from Physical Science and Commerce streams"
        ]
    }
    return details

if __name__ == "__main__":
    faculty_details = get_faculty_details()
    for key, value in faculty_details.items():
        print(f"{key}: {value}")
