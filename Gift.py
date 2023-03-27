class Gift:
    def __init__(self, name="", gender="不限", age_range="不限", hobby="", is_real=False, volume=0, price_range="不限"):
        """
        :param name: str, 礼物名称
        :param gender: str, 适合性别（"男"、"女"、"不限"）
        :param age_range: str, 适合年龄范围（"幼年"、"少年"、"青年"、"中年"、"老年"、"不限"）
        :param hobby: str, 适合爱好
        :param is_real: bool, 是否为实物
        :param volume: float, 实物体积，如果不是实物则为0
        :param price_range: str, 适合价格区间（"100元以下"、"100-500元"、"500-1000元"、"1000-5000元"、"5000元以上"、"不限"）
        """
        self.name = name
        self.gender = gender
        self.age_range = age_range
        self.hobby = hobby
        self.is_real = is_real
        self.volume = volume
        self.price_range = price_range

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getGender(self):
        return self.gender

    def setGender(self, gender):
        self.gender = gender

    def getAgeRange(self):
        return self.age_range

    def setAgeRange(self, age_range):
        self.age_range = age_range

    def getHobby(self):
        return self.hobby

    def setHobby(self, hobby):
        self.hobby = hobby

    def isReal(self):
        return self.is_real

    def setReal(self, is_real):
        self.is_real = is_real

    def getVolume(self):
        return self.volume

    def setVolume(self, volume):
        self.volume = volume

    def getPriceRange(self):
        return self.price_range

    def setPriceRange(self, price_range):
        self.price_range = price_range

    def is_suitable_for_recipient(self, recipient):
        """
        判断礼物是否适合收礼者
        :param recipient: Recipient类对象, 收礼者
        :return: bool, 是否适合
        """
        if self.gender != "不限" and self.gender != recipient.gender:
            # 不限性别或者适合该性别
            return False
        if self.age_range != "不限" and self.age_range != recipient.get_age_range():
            # 年龄范围不符
            return False
        if self.hobby != "不限" and self.hobby != recipient.hobby:
            # 不限爱好或者适合该爱好
            return False
        return True
