# Quote DB

import os
import sqlite3
import datetime
import random

# Make a database connection
db_filename = 'backend.db'
db = sqlite3.connect(db_filename)

def random_troll():
	cur = db.cursor()
	cur.execute("SELECT troll_id FROM troll;")
	troll_list = cur.fetchall()

	troll_id = random.choice(troll_list)[0]

	try:
		cur.execute("SELECT * from troll WHERE troll_id = ?;", (troll_id,))
		troll_comment = cur.fetchone()
		troll_comment_string = ("%s (%s)" % (troll_comment[1], troll_comment[0]))
		return(troll_comment_string)
	except:
		return("Troll DB error (%s)" % troll_id)

def lookup_by_troll_text(troll_text):
	cur = db.cursor()
	cur.execute("SELECT troll_id FROM troll WHERE troll_comment LIKE ?", ('%'+troll_text+'%',))
	trolls_requested = cur.fetchall()

	troll_number_list = []

	for item in trolls_requested:
		troll_number_list.append(str(item[0]).lower())

	troll_number_list_string = "".join(str(troll_number_list))[1:-1]

	if troll_number_list_string != "":
		troll_number_list_string = "Relevant Trolls: %s." % troll_number_list_string
	else:
		troll_number_list_string = "No relevant trolls."

	return troll_number_list_string


def lookup_by_troll_number(troll_number):
	cur = db.cursor()
	try:
		cur.execute("SELECT * from troll WHERE troll_id = ?", (troll_number,))
		troll_requested = cur.fetchone()
		troll_string = ("%s (%s)" % (troll_requested[1], troll_number))
		return(troll_string)
	except:
		return("Troll not found.")