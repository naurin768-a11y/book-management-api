from fastapi import FastAPI
import database

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "Book Management API"
    }

@app.get("/books")
def get_books():

    return database.get_all_books()


@app.get("/books/{name}")
def search_book(name: str):

    book = database.search_book(name)

    if book:

        return book

    return {
        "message": "Book not found!"
    }


@app.post("/books")
def add_book( name: str, author: str, year: int, genre: str, price:float):

    database.insert_book( name, author, year, genre,price)

    return {
        "message": "Book added successfully!"
    }


@app.delete("/books/{name}")
def delete_book(name: str):

    result = database.delete_book(name)

    if result:

        return {
            "message": "Book deleted successfully!"
        }

    return {
        "message": "Book not found!"
    }


@app.put("/books/{name}/price")
def update_price(
    name: str,
    new_price: float
):

    result = database.update_price(
        name,
        new_price
    )

    if result:

        return {
            "message": "Price updated successfully!"
        }

    return {
        "message": "Book not found!"
    }