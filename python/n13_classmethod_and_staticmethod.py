class ClassTest:
    def instance_method(self):
        print(f"called the instane_method of {self}")

    # this method would br the class itself. Used for factory method.
    @classmethod
    def class_method(cls):
        print(f"called class_method of {cls}")

    @staticmethod
    def static_method():
        print(f"called static_method")


test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)

ClassTest.class_method()

ClassTest.static_method()


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighting {self.weight}g>"

    @classmethod
    def hardcover(cls, name, page_weight):
        # here in place of cls we can use Book
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


print(Book.TYPES)

book = Book("Harry Potter", "hardcover", 1500)

book2 = Book.hardcover("Harry Potter", 1500)
print(book2)
