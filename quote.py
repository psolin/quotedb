# Quote DB

import sqlite3
import random
import os


def db_connection():
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(project_path, "quotedb/backend.db")
    return sqlite3.connect(db_path)


def random_quote():
    db = db_connection()
    cur = db.cursor()
    cur.execute("SELECT quote_id FROM quote;")
    quote_list = cur.fetchall()

    quote_id = random.choice(quote_list)[0]

    try:
        cur.execute("SELECT * from quote WHERE quote_id = ?;", (quote_id,))
        quote_comment = cur.fetchone()
        quote_comment_string = ("%s (%s)" % (quote_comment[1], quote_comment[0]))
        return quote_comment_string
    except sqlite3.ProgrammingError:
        return "quote DB error (%s)" % quote_id


def lookup_by_quote_text(quote_text):
    db = db_connection()
    cur = db.cursor()
    cur.execute("SELECT quote_id FROM quote WHERE quote_comment LIKE ?", ('%' + quote_text + '%',))
    quotes_requested = cur.fetchall()

    quote_number_list = []

    for item in quotes_requested:
        quote_number_list.append(str(item[0]).lower())

    quote_number_list_string = "".join(str(quote_number_list))[1:-1]

    if quote_number_list_string != "":
        quote_number_list_string = "Relevant quotes: %s." % quote_number_list_string
    else:
        quote_number_list_string = "No relevant quotes."

    return quote_number_list_string


def lookup_by_quote_number(quote_number):
    db = db_connection()
    cur = db.cursor()
    try:
        cur.execute("SELECT * from quote WHERE quote_id = ?", (quote_number,))
        quote_requested = cur.fetchone()
        quote_string = ("%s (%s)" % (quote_requested[1], quote_number))
        return quote_string
    except sqlite3.ProgrammingError:
        return "quote not found."
