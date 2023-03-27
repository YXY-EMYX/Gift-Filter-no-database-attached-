class Recipient:
    def __init__(self, gender, age, hobby):
        self._gender = gender
        self._age = age
        self._hobby = hobby

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @property
    def hobby(self):
        return self._hobby

    @hobby.setter
    def hobby(self, hobby):
        self._hobby = hobby

    def get_age_range(self):
        if self._age < 6:
            return "幼年"
        elif self._age < 18:
            return "少年"
        elif self._age < 28:
            return "青年"
        elif self._age < 40:
            return "青年"
        elif self._age < 60:
            return "中年"
        else:
            return "老年"
