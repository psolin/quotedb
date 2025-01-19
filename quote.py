import sqlite3
import random
import os


def db_connection():
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(project_path, "quotedb/backend.db")
    return sqlite3.connect(db_path)


def random_quote():
    with db_connection() as db:
        cur = db.cursor()
        cur.execute("SELECT quote_id FROM quote;")
        quote_list = cur.fetchall()
        quote_id = random.choice(quote_list)[0]

        try:
            cur.execute("SELECT * FROM quote WHERE quote_id = ?;", (quote_id,))
            quote_comment = cur.fetchone()
            return f"{quote_comment[1]} ({quote_comment[0]})"
        except sqlite3.ProgrammingError:
            return f"quote DB error ({quote_id})"


def lookup_by_quote_text(quote_text):
    with db_connection() as db:
        cur = db.cursor()
        cur.execute("SELECT quote_id FROM quote WHERE quote_comment LIKE ?", (f"%{quote_text}%",))
        quotes_requested = cur.fetchall()

        quote_number_list = [str(item[0]).lower() for item in quotes_requested]
        quote_number_list_string = ", ".join(quote_number_list)

        if quote_number_list_string:
            return f"Relevant quotes: {quote_number_list_string}."
        else:
            return "No relevant quotes."


def lookup_by_quote_number(quote_number):
    with db_connection() as db:
        cur = db.cursor()

        try:
            cur.execute("SELECT * FROM quote WHERE quote_id = ?", (quote_number,))
            quote_requested = cur.fetchone()
            return f"{quote_requested[1]} ({quote_number})"
        except sqlite3.ProgrammingError:
            return "quote not found."
