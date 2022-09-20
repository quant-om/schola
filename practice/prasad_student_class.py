class Student:


    def __init__(self, name):
        self.name = name
        self.sclass = None
        self.total_marks = 0

        self.quarterly_exams= {
            "quarter-1": {
                "maths": None,
                "science": None,
                "biology": None
            },
            "quarter-2": {
                "maths": None,
                "science": None,
                "biology": None
            },
            "quarter-3": {
                "maths": None,
                "science": None,
                "biology": None
            },
            "quarter-4": {
                "maths": None,
                "science": None,
                "biology": None
            },
        }


    def add_marks(self, sclass, qtr, math_marks, science_marks, biology_marks):
        self.sclass = sclass
        self.quarterly_exams[qtr]["maths"] = math_marks 
        self.quarterly_exams[qtr]["science"] = science_marks
        self.quarterly_exams[qtr]["biology"] = biology_marks

        self.total_marks += math_marks + science_marks + biology_marks

st = Student("prasad")
st.add_marks(10,"quarter-1", 90, 70, 80)

print("The total marks of the student is", st.total_marks)

