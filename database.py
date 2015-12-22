import sqlite3 as lite
import pandas as pd

con = lite.connect('database.db')

# Select all rows and print the result set one row at a time
with con:

  cur = con.cursor()
  #create cities 2 table
  con.execute("CREATE TABLE cities2 (name text, state text)")
  #Insert data into cities 2 table
  con.execute("INSERT INTO cities2 ('Las Vegas', 'NV')")
  con.execute("INSERT INTO cities2 ('Atlanta', 'GA')")

  #create weather 2 table
  con.execute("CREATE TABLE weather2 (City text, year integer, warm_month text, cold_month text');")
  #Insert data into weather 2 table
  con.execute("INSERT INTO weather2 ('Las Vegas', '2013', 'July', 'December')")
  con.execute("INSERT INTO weather2 ('Atlanta', '2013', 'July', 'January')")

  #Join cities2 & weather2
  con.execute("SELECT name, state, year, warm_month, cold_month FROM cities2 INNER JOIN weather2 ON name = city;")

  #Load into Panda Dataframe
  cur.execute("SELECT * FROM cities")
  rows = cur.fetchall()
  cols = [desc[0] for desc in cur.description]
  df = pd.DataFrame(rows, columns=cols)

print "The cities that are warmest in July are %s & %s" %(df[0], df[1])
