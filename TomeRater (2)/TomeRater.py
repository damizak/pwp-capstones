class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

# Creates change_email() which updates User email
    def change_email(self, address):
        self.email = address
        print ("The user {name} email has been updated to {new_email}".format(
            name=self.name, new_email=self.email))

    def __repr__(self):
        return "User {} , email {} , books read: {}".format(self.name, self.email, self.books)

# Creates __eq__ method to define comparison between users
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False
# Creates read Book method

    def read_book(self, book, rating=None):
        self.books[book] = rating
# Creates method to calculate the average rating of a User

    def get_average_rating(self):
        total = 0
# For Loop that Iterates over each  rating and calculates average of total
        for ratings in self.books.values():

            if type(ratings) == int:

                total += ratings

        return total / len(self.books.values())


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "Isbn has been updated to {}".format(new_isbn)

    def add_rating(self, new_rating):
        if new_rating >= 0 and new_rating <= 4:
            self.ratings.append(new_rating)
        else:
            print("invalid Rating")


# Creates __eq__ method to define comparison between Books
    def __eq__(self, other_user):
        if self.title == other_user.title and self.isbn == other_user.isbn:
            return True
        else:
            return False

    def __lt__(self, other_user):
        if self.title < other_user.title:
            return True
        else:
            return False

    def __gt__(self, other_user):
        if self.title > other_user.title:
            return True
        else:
            return False


# For Loop that Iterates over each  rating and calculates average of total
    def get_average_rating(self):
        total = 0
        for rating in self.ratings:
            if rating == int:
                total += rating

        return rating / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return self.title


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {} ".format(self.title, self.level, self.subject)


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}
        self.isbns = []

    def create_book(self, title, isbn):
        # Checks if isbn exist, if not create book
        if isbn in self.isbns:
            print ("Duplicate ISBN")
            return
        else:
            new_book = Book(title, isbn)
            self.isbns.append(isbn)
            return new_book

    def create_novel(self, title, author, isbn):
        # Checks if isbn exist, if not create book
        if isbn in self.isbns:
            print ("Duplicate ISBN")
            return
        else:
            new_fiction = Fiction(title, author, isbn)
            self.isbns.append(isbn)
            return new_fiction

    def create_non_fiction(self, title, subject, level, isbn):
        # Checks if isbn exist, if not create book
        if isbn in self.isbns:
            print ("Duplicate ISBN")
            return
        else:
            new_non_fiction = Non_Fiction(title, subject, level, isbn)
            self.isbns.append(isbn)
            return new_non_fiction

# Creates add_book_to_user method
    def add_book_to_user(self, book, email, rating=None):
        try:
            new_user = self.users[email]
        except KeyError:
            print("No User with email {}".format(email))
        else:
            new_user.read_book(book, rating)
            if rating is not None:
                book.add_rating(rating)

            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1

# Creates add_user method,
    def add_user(self, name, email, user_books=None):

        # Checks if user already exist
        if email in self.users.keys():
            print ("User already exists")
            return
        # Checks if email is valid if valid, add user and return
        else:
            checks = [".com", ".edu", ".org"]
            x = 0
            while x < len(checks):
                if checks[x] in email and "@" in email:
                    new_user = User(name, email)
                    self.users[email] = new_user
                    if user_books is not None:
                        for book in user_books:
                            TomeRater.add_book_to_user(self, book, email)
                    return
                else:
                    x += 1

        print ("invalid Email")
        return


# Creates method to print the book catalog

    def print_catalog(self):
        for book in self.books.keys():
            print (book)
# Creates method to print all users

    def print_users(self):
        for user in self.users.values():
            print (user)
# Creates method to return the most read book

    def most_read_book(self):
        total = 0
        most_read = ""

        for key, value in self.books.items():
            if value > total:
                most_read = key
                total = value
        return most_read
# Creates Method to return the highest rated book

    def highest_rated_book(self):
        rating = 0
        highest_rated = ""

        for book in self.books.keys():
            avg_rating = book.get_average_rating()

            if avg_rating > rating:
                rating = avg_rating
                highest_rated = book
        return highest_rated
# Create method to return user with the highest rating

    def most_positive_user(self):
        rating = 0
        highest_rated = ""

        for user in self.users.values():

            avg_rating = user.get_average_rating()

            if avg_rating > rating:
                rating = avg_rating
                highest_rated = user
        return highest_rated
# Create method to return most read book
    def get_n_most_read_books(self, n):
        top_n_books = []
        top_n_books_descending = []

        for x in sorted(self.books.values()):
            for key, value in self.books.items():
                if value == x and key not in top_n_books:
                    top_n_books.append(key)

        for y in range(-1, -1 - n, -1):
            try:
                top_n_books_descending.append(top_n_books[y])
            except IndexError:
                break
        print (top_n_books_descending)
