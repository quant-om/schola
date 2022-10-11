class Student:
    def __init__(self, name):
        print("this is init method")

        self.name = name
        self.sclass = None
        self.total_marks = 0
        self.quarter_marks = 0
        
        self.quarterly_marks = {
            "quarter-1" : {
                "maths" : None,
                "science" : None,
                "biology" : None,
                "quarter_marks" : 0
            },
            "quarter-2" : {
                "maths" : None,
                "science" : None,
                "biology" : None,
                "quarter_marks" : 0
            },
            "quarter-3" : {
                "maths" : None,
                "science" : None,
                "biology" : None,
                "quarter_marks" : 0
            },
            "quarter-4" : {
                "maths" : None,
                "science" : None,
                "biology" : None,
                "quarter_marks" : 0
            },
        }

    def get_name(self):
        return self.name

    def get_quart_marks1(self, quart):
        return self.quarterly_marks[quart]["quarter_marks"]

    

    def get_quart_marks(self, quart):
        val = 0
        for key in self.quarterly_marks[quart]:
            kval = self.quarterly_marks[quart][key]
            if kval is not None:
                val += self.quarterly_marks[quart][key]

        return val



    def add_marks(self, sclass, quart, maths_marks, sci_marks, bio_marks):

        self.sclass = sclass
        self.quarterly_marks[quart]["maths"] = maths_marks
        self.quarterly_marks[quart]["science"] = sci_marks
        self.quarterly_marks[quart]["biology"] = bio_marks

        self.total_marks += maths_marks + sci_marks + bio_marks
        self.quarter_marks = maths_marks + sci_marks + bio_marks

    



st = Student("quantom")
st.add_marks(9, "quarter-1", 90, 80, 70)
st.add_marks(9, "quarter-2", 80, 45, 75)
st.get_quart_marks1("quarter-1")

print(f"The total marks of the student is {st.total_marks}")
print(f"The quarterly-1 marks of the student are {st.quarterly_marks['quarter-1']}")


print(f"The quarterly-1 marks of the student is {st.get_quart_marks('quarter-1')}")
print(f"The quarterly-2 marks of the student is {st.get_quart_marks('quarter-2')}")
print(f"The quarterly-3 marks of the student is {st.get_quart_marks('quarter-3')}")

print(f"The quarter marks of the student is {st.get_quart_marks1('quarter-1')}")



st2 = Student("python")






print(f"The name of the student is {st2.get_name()}")



