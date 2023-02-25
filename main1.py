from collections import UserDict, UserList

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'

class Name(Field):
    pass

class Phone(Field):
    pass

class Record(Name, Phone):

    phone_list =[]

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


        if phone:
            self.phone_list.append(phone)

    def get_name(self):
        self.value = Name

    def get_phone(self):
        self.value = Phone

    def add_phone(self, phone):
        self.phone = phone
        self.phone_list.append(self.phone)
    def del_phone(self, phone):
        self.phone = phone
        if phone == phone:
            self.phone_list.remove(self.phone)

    def change_phone(self, phone, new_phone):
        self.phone = phone
        self.new_phone = new_phone
        if phone in ab.phone_list:
            self.phone_list.remove(self.phone)
            self.phone_list.append(self.new_phone)




class AddressBook(UserDict, Record):
    def add_record(self, rec):
        self.data[rec.name.value] = rec
        return self.data



if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    phone_1 = Phone("121241242")
    phone_2 = Phone('1234567890414124')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    ab.add_phone(phone_1)
    #ab.del_phone(phone_1)
    #ab.change_phone(phone_1 , phone_2)
    print(ab.phone_list)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phone_list, list)
    assert isinstance(ab['Bill'].phone_list[0], Phone)
    assert ab['Bill'].phone_list[0].value == '1234567890'
    print('All Ok)')
