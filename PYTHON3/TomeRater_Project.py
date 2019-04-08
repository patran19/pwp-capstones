class User(object):
    """
	Contructors for name, email, books
        Functins for get_email, change_email, read_book, and get_average_rating
    """ 
    def __init__(self, name, email):
        """
        Contructor for name, email and books, name is a string, email is a string
        Books is a dictionary  which will help to map a book object
        """
        if email.find("@") == -1 or (email.find(".com") == -1 and email.find(".edu") == -1 and email.find(".org") == -1):
            print("The email {email} is not valid, please re-check it has an @ and a .com, .edu, or .org domain.".format(email=email))
        else:
            self.name = name  
            self.email = email   
            self.books = {} 
    def get_email(self):
        return self.email
    def change_email(self, new_email):
        """
        Print a message regarding email changed
        """
        self.email = new_email
        return "Thank you for updating your email.  Your new email is: " + self.email
    def __repr__(self):
        """
        Return a  readable message giving the name, email, and Book read.        
        The self.books is what is needed 
        """       
        message_statement = "Username: " + self.name + ". Email Address: " + self.email + ". Books Read: " + str(list(self.books.values()))
        return message_statement
        
    def __eq__(self, other_user):
        if (other_user == self.name):
            other_user == self
    def read_book(self, book, rating=None):
        self.books[book] = rating
    def get_average_rating(self):
        average_rating = 0
        ratings_total = 0
        for rating in self.books.values():
            print(rating)
            ratings_total += rating
        average_rating = ratings_total / len(self.books)
        return average_rating

class Book:
    def __init__(self, title, isbn):
        """
        ISBN is an interger number
        """
        self.title = title #title is a string
        self.isbn = isbn 
        self.rating = []
    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "This book's ISBN has been updated. It's now: " + str(new_isbn)
    def add_rating(self, rating):
        if rating and 0 <= rating <= 4:
            self.rating.append(rating)
        else:
            print("Invalid Rating")
    def __eq__(self, book_object):
        if book_object.title == self.title and book_object.isbn == self.isbn:
            book_object = self
    def get_average_rating(self):
        average_rating = 0
        ratings_totals = 0
        for rating in self.ratings:
            ratings_totals += rating
        average_rating = ratings_totals / len(self.ratings)
        return average_rating
    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    def get_author(self):
        return self.author
    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author = self.author)

class NonFiction(Book):
    """
    subject and level  are strings
    """ 
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject  
        self.level = level  
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
    def __repr__(self):
        return "{title}, a {level} book on {subject}".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater:
    """
        dictionaries =  self.users   and self.books
        dictionary maps email to user object
        dictionary maps book object to number of users that had read it
    """
    def __init__(self):
        self.users = {}   
        self.books = {}  
    def create_book(self, title, isbn):
        return Book(title, isbn)
    def create_novel(self, title, author, isbn):
        new_fiction = Fiction(title, author, isbn)
        return new_fiction
    def create_non_fiction(self, title, subject, level, isbn):
        nonfiction_object = NonFiction(title, subject, level, isbn)
        return nonfiction_object
        

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            user = self.users.get(email, None)
            user.read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {}".format(email))
    def add_user(self, name, email, user_books = None):
        new_user = User(name,email)
        self.users[email] = new_user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)
                #_-- saucy girl <-- <-
    def print_catalog(self):
        for key in self.books.keys():
            print(key)
    def print_users(self):
        for value in self.users.keys():
            print(value)
    def most_read_book(self):
        read_most = None
        read_count = 0
        for book in self.books.keys():
            if self.books[book] > read_count:
                read_count = self.books[book]
            if self.books[book] == read_count:
                read_most = book
        return read_most
         
    def highest_rated_book(self):
        book_best = None
        highest_rating = 0
        for book in self.books.keys():
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                book_best = book
        return book_best
                #---
        book_best = ""
        for book in self.books.keys():
            book_object = Book.get_average_rating(self)
            if book_object > book_best:
                book_object = book_best
        return book_best
    def most_positive_user(self):
        highest_rating = 0
        highest_user = None
        for user in self.users.values():
            average = User.get_average_rating(self)
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                highest_user = user
        return highest_user
         

