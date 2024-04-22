class Pruefling:
    def __init__(self, eye_color, hair_style, test_grade, firstname, lastname):
        self.final_grade = 6.0
        self.eye_color = eye_color
        self.hair_style = hair_style
        self.test_grade = test_grade
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return (f"{self.lastname}, {self.firstname} hat die Note: "
                f"{self.final_grade} erreicht. \n"
                f"(Augenfarbe: {self.eye_color}, Haarlänge: {self.hair_style})")