"""
Example of MCP course tools.
Each function will be called by LLM.
"""
from typing import List, Dict

def list_majors() -> List[str]:
    """
    Returns a list of available majors.
    """
    // TODO: extract info from PDF or database in future
    return [
        "Computer Science",
        "Applied Artificial Intelligence"
    ]

def get_semester_courses(major: str, semester: int) -> List[str]:
    """
    Returns a list of courses for a given major and semester.
    major: Name of the major
    semester: Semester number (1-8)
    """
    dummy_data = {
        "Computer Science": {
            1: ["Introduction to Programming", "Discrete Mathematics"],
            2: ["Data Structures", "Computer Architecture"],
            3: ["Algorithms", "Operating Systems"],
            4: ["Database Systems", "Software Engineering"],
            5: ["Computer Networks", "Artificial Intelligence"],
            6: ["Machine Learning", "Web Development"],
            7: ["Mobile App Development", "Cloud Computing"],
            8: ["Capstone Project", "Cybersecurity"]
        },
        "Applied Artificial Intelligence": {
            1: ["Introduction to AI", "Linear Algebra"],
            2: ["Probability and Statistics", "Programming for AI"],
            3: ["Machine Learning Basics", "Data Mining"],
            4: ["Neural Networks", "Natural Language Processing"],
            5: ["Computer Vision", "Reinforcement Learning"],
            6: ["AI Ethics", "Robotics"],
            7: ["Advanced Machine Learning", "AI in Healthcare"],
            8: ["AI Capstone Project", "AI for Social Good"]
        }
    }
    return dummy_data.get(major, {}).get(semester, [])

def get_course_details(course_name: str) -> Dict[str, str]:
    """
    Returns details of a given course.
    course_name: Name of the course
    """
    # TODO: extract info from PDF or database in future
    return {
        "name": course_name,
        "description": f"This is a detailed description of the course {course_name}.",
        "content": "Detailed syllabus and topics covered in the course.",
        "exam": "Exam format and evaluation criteria."
    }