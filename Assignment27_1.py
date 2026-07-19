class BookStore:
    
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Accpet(self):
        self.Name = print("Book name : ")
        self.Author = print("Author name : ")

    def display(self):
        print(self.Name,"by",self.Author,"No of books : ",BookStore.NoOfBooks)

def main():
    Bobj1 = BookStore("Linux System Programming","Robert Love")
    Bobj1.display()

    Bobj2 = BookStore("C programming","Dennis Ritchie")
    Bobj2.display()
    
    Bobj3 = BookStore("Python Programming","Guido van Rossum")
    Bobj3.display()

if __name__ == "__main__":
    main()
