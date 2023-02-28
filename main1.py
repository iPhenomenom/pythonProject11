import datetime
import re
from collections import UserDict, UserList

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'


class Name(Field):
    pass

class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if re.search(r"\+\d{3}\(\d{2}\)\d{3}\-\d{2}\-\d{2}|\+\d{3}\(\d{2}\)\d{3}\-\d{1}\-\d{3}", new_value):
            self.__value = new_value
        else:
            raise TypeError("Invalid number phone")

class Birtday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if re.search(r"\d{2}\-\d{2}\-\d{4}", new_value):
            self.__value = new_value
        else:
            raise TypeError("Invalid Data Info")

class Record(Name, Phone , Birtday):

    phone_list =[]




    def __init__(self, name, phone, date):
        self.name = name
        self.phone = phone
        self.date = date


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

    def days_to_birthday(self, date):


        if date == None:
            pass

        else:
            test_date = str(date)
            now = datetime.datetime.now()
            then = datetime.datetime.strptime(test_date, "%d-%m-%Y")
            delta1 = datetime.datetime(now.year, then.month, then.day)
            delta2 = datetime.datetime(now.year + 1, then.month, then.day)

            result = ((delta1 if delta1 > now else delta2) - now).days
            print(f'Days to Birthday: {result}')
            #self.phone_list.append(f"Days to Birthday: {result}")

class AddressBook(UserDict, Record):


    def add_record(self, rec):
        self.data[rec.name.value] = rec
        return self.data

    def iterator(self):
        a = ab.phone_list
        index = 0
        yield a[index]
        index += 1

if __name__ == '__main__':
    name = Name('Bill')

    phone = Phone('+380(96)163-50-10')
    phone_1 = Phone('+380(96)163-50-20')
    phone_2 = Phone('+380(96)163-50-13')

    date = Birtday('25-03-2010')

    rec = Record(name, phone, date)
    rec.days_to_birthday(date)

    ab = AddressBook()
    ab.add_record(rec)
    ab.iterator()

    #ab.del_phone(phone_1)
    #ab.change_phone(phone_1 , phone_2)
    print(ab.phone_list)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phone_list, list)
    assert isinstance(ab['Bill'].phone_list[0], Phone)
    assert ab['Bill'].phone_list[0].value == '+380(96)163-50-10'
    print('All Ok)')
