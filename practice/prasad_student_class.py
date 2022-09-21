class Student:
    """
    Student class for calculating Marks of a Student.
    """
    def __init__(self, name):
        self.name = name
        self.sclass = None
        self.total_marks = 0
        self.qter_marks = 0

        self.quarterly_exams= {
            "quarter-1": {
                "maths": None,
                "science": None,
                "biology": None,
                "quarter_marks": 0
            },
            "quarter-2": {
                "maths": None,
                "science": None,
                "biology": None,
                "quarter_marks": 0
            },
            "quarter-3": {
                "maths": None,
                "science": None,
                "biology": None,
                "quarter_marks": 0
            },
            "quarter-4": {
                "maths": None,
                "science": None,
                "biology": None,
                "quarter_marks": 0
            },
        }


    def get_name(self):
        """
        Get the name of the student
        Returns : returns the name of the student
        """
        return self.name


    def get_quart_marks1(self, qtr):
        return self.quarterly_exams[qtr]["quarter_marks"]


    def add_quarter_marks1(self, qtr, qter_maths, qter_science, qter_biology):

        self.quarterly_exams[qtr]["quarter_marks"] = qter_maths
        self.quarterly_exams[qtr]["quarter_marks"] = qter_science
        self.quarterly_exams[qtr]["quarter_marks"] = qter_biology

        self.qter_marks += qter_maths + qter_science + qter_biology

    def get_quart_marks(self, qtr):
        """
        Get the marks of a particular quarter.

        qrt: (string) Name of the quarter
        Returns : (int) total marks of the quarter
        """
        # iterate a dictionary
        val = 0
        for key in self.quarterly_exams[qtr]:
            kval = self.quarterly_exams[qtr][key]
            if kval is not None:
                val += kval
        
        return val


    def add_marks(self, sclass, qtr, math_marks, science_marks, biology_marks):
        self.sclass = sclass
        self.quarterly_exams[qtr]["maths"] = math_marks 
        self.quarterly_exams[qtr]["science"] = science_marks
        self.quarterly_exams[qtr]["biology"] = biology_marks

        self.total_marks += math_marks + science_marks + biology_marks
        


st = Student("prasad")
st.add_marks(10,"quarter-1", 90, 70, 80)
st.add_marks(9, "quarter-2", 77, 68, 82)
st.add_quarter_marks1("quarter-1", 60, 60, 60)


print("The total marks of the student is", st.total_marks)
print(f"The quarterly-1 marks of the student are {st.quarterly_exams['quarter-1']}")

print(f"The quarterly-1 marks of the student is {st.get_quart_marks('quarter-1')}")
print(f"The quarterly-2 marks of the student is {st.get_quart_marks('quarter-2')}")
print(f"The quarterly-3 marks of the student is {st.get_quart_marks('quarter-3')}")

print("The Quarterly marks of the student is", st.qter_marks)

st2 = Student("python")
print(f"The name of the studenqt is {st2.get_name()}")
print(f"The quarterly-1 marks of the student is {st2.get_quart_marks('quarter-1')}")
print(f"The quarter-2 marks of the student is {st.get_quart_marks('quarter-2')}")
