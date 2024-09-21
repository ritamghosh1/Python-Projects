# Creating Library Management System Class
class Library :
    def __init__(self):
        self.books = []
        self.no_Books = len(self.books)
        print(f"New book space is created . Currently {self.no_Books} books are in the Library . Please enter the book detais ")
    
    def add_books(self,Title):
        self.Title = Title
        self.books.append(Title)
        print(f"The {self.Title} book is added")
    
    def remove_books(self,Title):
        if not self.Title == Title: print(f"The {Title} book does not exist")
        else : 
            print(f"The {self.Title} book is removed")
            self.books.remove(Title)
    
    def print_books(self):
        print("This are the following books that exist in the Library")
        for book in self.books:
            print(book)

l1 = Library()
l1.add_books("Harry Potter")
l1.add_books("To Kill a Mockingbird")
l1.add_books("1984")
l1.print_books()

        


        