def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor Cannot be Zero.")

    return dividend / divisor


grades = [45, 78, 90, 56, 56, 78]

try:
    average = divide(sum(grades), len(grades))
    print(f"The average grade is {average}")
except ZeroDivisionError as e:
    print("There are no grades yet in your list.")
except ValueError:
    print("Error Here")
else:
    print(f"The average grade is {average}.")
finally:
    print("Thank you!")

class TooManyPagesReadError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Book:
    def __init__(self, name: str, page_count: int) -> None:
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self) -> str:
        return f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}"

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(f"You read two many pages")
        self.pages_read += pages
        print(
            f"You have now read {self.pages_read} page out of {self.page_count}")

python101 =  Book("Python 101", 50)
python101.rade(35)
python101.rade(50)