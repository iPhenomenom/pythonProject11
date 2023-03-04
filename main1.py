import datetime
import re
from collections import UserDict, UserList
import pickle
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

    def add_name(self):
        self.name = name
        self.phone_list.append(self.name)
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
            self.phone_list.append(f"{result} Day ")
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



    def save(self):
        with open("save.txt", "a") as file:
            file.write(str(f"Name: {name}, Phone: {phone}, Birthday: {date}\n"))

    def load(self):


        with open("save.txt", "r") as file:
            for line in file.readlines():
                if line.startswith("Phone"):
                    ab.phone_list = line

            return ab.phone_list
    def find(self):

        word = input(f"Find number : ")

        inp = open("save.txt").readlines()

        for i in iter(inp):
            if word in i:
                print(i)

"""
    def iterator(self, n=2):  # параметр n - по замовчуванню 2
        index = 1
        print_block = '-' * 50 + '\n'  # блоки виводу, пагінація
        for record in self.data.values():  # ітеруємось по словнику АдресБук
            print_block += str(record) + '\n'
            if index < n:  # якщо індекс меньше нашої n - то додаюмо запис в нашу строку print_block
                index += 1
            else:
                yield print_block  # якщо ж індекс більше чим параметр n - то повертаємо всі записи що зібрали
                index, print_block = 1, '-' * 50 + '\n'
        print(print_block)
        yield print_block  # повертаємо що залишилось


    def show_all(*args):
        result = f'Contacts list:\n'
        print_list = CONTACTS.iterator()  # викликаємо метод ітератор в нашіх книги контактів
        for item in print_list:
            result += f'{item}'
        print(result)
        return result
"""
if __name__ == '__main__':
    a = input(str("Input Name, Phone, Birthday : ")).split(' ')
    #print(a)
    name = Name(a[0])
    phone = Phone(a[1])
    date = Birtday(a[2])


    rec = Record(name, phone, date)
    #rec.add_name()
    rec.days_to_birthday(date)


    ab = AddressBook()

    ab.load()
    #print(rec.phone_list)
    rec.add_phone(phone)
    ab.add_record(rec)
    ab.save()
    ab.find()

    #ab.iterator()
    #ab.show_all()
    #ab.del_phone()
    #ab.change_phone(phone_1 , phone_2)


    #assert isinstance(ab['Bill'], Record)
    #assert isinstance(ab['Bill'].name, Name)
    #assert isinstance(ab['Bill'].phone_list, list)
    #assert isinstance(ab['Bill'].phone_list[0], Phone)
    #assert ab['Bill'].phone_list[0].value == '+380(96)163-50-10'

    #print('All Ok)')