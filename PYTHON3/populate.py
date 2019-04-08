

from TomeRater_Project import *
#import TomeRater as TR

Tome_Rater = TomeRater()

#test_users = TomeRater.add_user("ClaireBookworm", "patran12@gmail.com", ["Hello"])
#test_books = TomeRater.most_read_book()
#TomeRater.add_user("Paul Tran", "paultran@sjsu.edu", ["Books", "novel1", "nonfiction1"])

#TomeRater.add_user("Paul Tran", "paultran@sjsu.edu")

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
print(book1.title)

novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
print(novel1.isbn)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 432555555)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 43556788)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")
print(Tome_Rater.print_users())
#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", [book1, novel1, nonfiction1])
#print("users......")
print(Tome_Rater.print_users())
#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 2)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 2)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 4)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 4)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 3)

print(Tome_Rater.books)
#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()
print(Tome_Rater.books)
print("Most positive user:  flag")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())

