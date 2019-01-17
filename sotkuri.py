import sqlite3
from sqlite3 import Error
import webbrowser
import time
import os
import csv
from random import randint
import random

id = 1
list = []
with open('scratch.csv') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		row = list.append(row)

		
def create_connection(database):
	try:
		conn = sqlite3.connect(database)
		return conn
	except Error as e:
		print(e)

	return None
		
def avaa_yksi_kategoria(conn, kategoria):
	cur = conn.cursor()
	cur.execute("SELECT * from data WHERE kategoria=?", (kategoria))

	rows = cur.fetchall()

	for row in rows:
		webbrowser.open(row[1])
		print(row[1])
	print("Sleeping for 7 seconds")
	time.sleep(7)
	print("Killing chrome.exe")
	os.system("taskkill /im chrome.exe /f")
		
def main():
	database = "urlit.db"

	conn = create_connection(database)
	with conn:
		for id in range(10):
			rand = random.randint(0,1374)
			print("-------- OPENING " + str(list[rand]) + " LINKS --------")
			avaa_yksi_kategoria(conn, list[rand])
			
if __name__ == '__main__':
	main()
