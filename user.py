from enum import Enum

class WeightCategory(Enum):
    """Weight categories based on BMI"""
    
    UNDERWEIGHT = 1
    NORMAL = 2
    OVERWEIGHT = 3
    OBESE = 4

class User(object):
    """App user class"""
    
    def __init__(self, name, sex, age, weight, height):
        self.name = name
        self.sex = sex
        self.age = age
        self.weight = weight
        self.height = height

    def get_bmi(self):
        """Metric system BMI formula"""
        return self.weight / (self.height/100)**2

    def get_category(self):
        """Weight categories assignment.
           source : https://en.wikipedia.org/wiki/Body_mass_index
        """
        bmi = self.get_bmi()
        if bmi < 18.5:
            return WeightCategory.UNDERWEIGHT
        elif bmi < 25:
            return WeightCategory.NORMAL
        elif bmi < 30:
            return WeightCategory.OVERWEIGHT
        else:
            return WeightCategory.OBESE 
    