from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]


@app.get("/books")
async def read_all_books():
    return BOOKS


# @app.get("/books/{dynamic_params}")
# async def read_all_books(dynamic_params: str):
#     return {"dynamic_params": dynamic_params}


# order matter !!!
# @app.get("/books/mybook")
# async def read_all_books():
#     return {"books title": "my favorite book"}



@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book['title'].casefold() == book_title.casefold():
            return book
    return None

# Query Params
@app.get("/books/")
async def read_books_by_category(category: str):
    result = []
    for book in BOOKS:
        if book['category'].casefold() == category.casefold():
            result.append(book)
    return result

# Query and path params
@app.get("/books/{author}/")
async def read_books_by_author_and_category(author: str, category: str):
    result = []
    for book in BOOKS:
        if book['author'].casefold() == author.casefold() and book['category'].casefold() == category.casefold():
            result.append(book)
    return result
