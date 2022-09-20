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

        #quart_marks = maths_marks + sci_marks + bio_marks
        self.total_marks += maths_marks + sci_marks + bio_marks

st = Student("quantom")
st.add_marks(9, "quarter-1", 90, 80, 70)

print(f"The total marks of the student is {st.total_marks}")


    