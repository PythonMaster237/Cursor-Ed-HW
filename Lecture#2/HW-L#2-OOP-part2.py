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

    def __str__(self):
        return f" {self.name} \n {self.last_name} \n {self.phone_number} \n {self.address} \n {self.email} \n \
{self.birthday} \n {self.age} \n {self.sex}"

    def to_list_params(self):
        dict_attrs = vars(self)
        for i in dict_attrs.items():
            print(f"{i[0]} - {i[1]}")


profile_1 = Profile("Alex", "Last", 2335344, "Down Street", "example@.com", "April 12", 24, "man")
#
# profile_1.to_list_params()

# print(profile_1)
