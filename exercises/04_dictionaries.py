"""
TODO:
Create dictionary for a book
"""
library = [
    {
        "title": "Harry Potter",
        "author": ["JK Rowling"]
    },
    {
        "title": "Align And Thrive",
        "author": ["Rivka Robinson"]
    },
    {
        "title": "Conducting Online Research on Amazon Mechanical Turk and Beyond",
        "author": ["Jonathon Robinson", "Leib Litman"] # List of strings for multiple authors
    }
]

for book in library:
    # .join() turns the author list into a nice string
    authors = ", ".join(book["author"])
    print(f"Book: {book['title']} | Authors: {authors}")