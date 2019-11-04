class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title}, {self.author},"
    def __repr__(self):
	    return f"Book({repr(self.title)},{repr(self.author)})"



def insertion_sort(books):
    for i in range(1,len(books)): # red square moves with i
        temp = books[i]
        j = i 

        while j >  0 and temp.author < books[j - 1].author:
            books[j] = books[j - 1]
            j -= i
        books[j] = temp


    return books

books = [
	Book("title5", "albert"),
	Book("title6", "Anna"),
	Book("title1", "author3"),
	Book("title3", "!author4"),
	Book("title2", "author5"),
	Book("title4", " author6"),
]

books_sorted = insertion_sort(books)

print(books_sorted)

