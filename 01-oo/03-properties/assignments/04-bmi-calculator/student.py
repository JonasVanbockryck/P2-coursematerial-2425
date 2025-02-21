class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.weight_in_kg = weight_in_kg
        self.height_in_m = height_in_m
        self.bmi = round((weight_in_kg / height_in_m**2), 2)
        self.category = None
    
    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self, value):
        if self.bmi < 18.5:
            self.__category = "underweight"
        elif self.bmi > 25:
            self.__category = "overweight"
        else:
            self.__category = "normal"


calc = BMICalculator(weight_in_kg=50, height_in_m=1.80)
print(calc.bmi)
print(calc.category)