class Student:
    """
    Student class for calculating Marks of a Student.
    """
    def __init__(self, name):
        """
        This is init method, the starting point of a class.

        name : (str) Students name
        """
        self.name = name
        self.sclass = None
        self.total_marks = 0

        self.quarterly_exams = {
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


    def get_quart_marks1(self, quart):
        return self.quarterly_exams[quart]["quarter_marks"]


    def get_quart_marks(self, quart):
        """
        Get the marks of a particular quarter.

        quart: (string) Name of the quarter
        Returns : (int) total marks of the quarter
        """
        # iterate a dictionary
        val = 0
        for key in self.quarterly_exams[quart]:
            kval = self.quarterly_exams[quart][key]
            if kval is not None:
                val += kval
        
        return val

    def add_marks(self, sclass, quart, maths_marks, sci_marks, bio_marks):
        """
        Adding marks to the student object

        sclass : (int) Students grade.
        quart  : (str) Quarter marks (quarter-1, quarter-2 etc)
        maths_marks: (int) maths marks in that quarter
        sci_marks : (int) science marks in that quarter
        bio_marks : (int) biology marks in that quarter
        """
        self.sclass = sclass
        self.quarterly_exams[quart]["maths"] = maths_marks
        self.quarterly_exams[quart]["science"] = sci_marks
        self.quarterly_exams[quart]["biology"] = bio_marks
        
        self.total_marks += maths_marks + sci_marks + bio_marks


st = Student("quantom")
st.add_marks(9, "quarter-1", 90, 80, 70)
st.add_marks(9, "quarter-2", 80, 45, 75)

print(f"The total marks of the student is {st.total_marks}")
print(f"The quarterly-1 marks of the student are {st.quarterly_exams['quarter-1']}")

print(f"The quarterly-1 marks of the student is {st.get_quart_marks('quarter-1')}")
print(f"The quarterly-2 marks of the student is {st.get_quart_marks('quarter-2')}")
print(f"The quarterly-3 marks of the student is {st.get_quart_marks('quarter-3')}")
    

st2 = Student("python")
print(f"The quarterly-1 marks of the student is {st2.get_quart_marks('quarter-1')}")
print(f"The name of the student is {st2.get_name()}")
