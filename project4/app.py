import pandas as pd

# Load the dataset
books_df = pd.read_csv('books.csv')

def search_books(keyword):
  
    keyword = keyword.lower()
    results = books_df[
        books_df['title'].str.lower().str.contains(keyword) |
        books_df['authors'].str.lower().str.contains(keyword) |
        books_df['publisher'].str.lower().str.contains(keyword)
    ]
    return results


def display_books(books):
   
    if books.empty:
        print("No books found.")
    else:
        for index, book in books.iterrows():
            print(f"Title: {book['title']}")
            print(f"Author: {book['authors']}")
            print(f"Average Rating: {book['average_rating']}")
            print(f"ISBN: {book['isbn']}")
            print(f"ISBN13: {book['isbn13']}")
            print(f"Language: {book['language_code']}")
            # Check if 'num_pages' column exists before printing
            if 'num_pages' in book:
                print(f"Number of Pages: {book['num_pages']}")
            print(f"Ratings Count: {book['ratings_count']}")
            print(f"Text Reviews Count: {book['text_reviews_count']}")
            print(f"Publication Date: {book['publication_date']}")
            print(f"Publisher: {book['publisher']}")
            print('-' * 40)

def main():
    print("Welcome to the Book Recommendation Program!")
    keyword = input("Enter a keyword to search for books: ")
    results = search_books(keyword)
    display_books(results)

if __name__ == "__main__":
    main()
