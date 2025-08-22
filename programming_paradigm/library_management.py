
class Book():

    def __init__(self , title , author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def is_available(self) -> bool:
        """Returns True if the book is not checked out."""
        return not self._is_checked_out
    
    def set_available(self):
        self._is_checked_out = False

    def set_not_available(self):
        self._is_checked_out = True



class Library ():
    def __init__(self):
        self._books = []

    def add_book(self, book:Book):
        self._books.append(book)

    def list_available_books(self):
        
        for book in self._books:
            if book.is_available():
                print(book.title , "by" , book.author)

    def _find_book_by_title(self, title: str):
        for b in self._books:
            if b.title == title:
                return b
        return None
    
    def check_out_book(self, title:str):
        book = self._find_book_by_title(title)
        if book in self._books and book.is_available():
            book.set_not_available()


    def return_book(self, title:str):
        book = self._find_book_by_title(title)
        if book in self._books and not book.is_available():
            book.set_available()
