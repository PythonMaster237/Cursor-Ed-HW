class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def to_list_params(self):
        dict_attrs = vars(self)
        for i in dict_attrs.items():
            print(f"{i[0]} - {i[1]}")


profile_1 = Profile("Alex", "Last", 2335344, "Down Street", "example@.com", "April 12", 24, "man")

profile_1.to_list_params()
