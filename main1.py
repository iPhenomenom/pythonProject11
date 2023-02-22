from collections import UserDict


class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'



a = Field(value=input())
#print(f"in Field {a.value}")


class Name(Field):
    pass


class Phone(Field):
    pass


class Record(Field):

    name = []
    phone = []

    def add_name(self):
        f = a.value.split()
        rec.name.append(f"Имя: {f[0]}")
        try:
            rec.phone.append(f"Номер: {f[1]}")
        except:
            print('нету телефона')


rec = Record(Field)
#print(f"in Record {a.value}")
rec.add_name()

print(rec.name)
print(rec.phone)


class AddressBook(Record, UserDict):

    phone_book = {}

    def add_record(self):
        f = a.value.split()
        try:
            g = dict([f])
            book.phone_book.update(g)
        except:
            print('Нету номера')




book = AddressBook(Record)
book.add_record()
print(book.phone_book)