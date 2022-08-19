# DataBase Management
import sqlite3 
conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()

# table is called filestable
# - varname: filestable, vartype: TEXT (could also be size)

# Table
def create_uploaded_filetable():
	c.execute('CREATE TABLE IF NOT EXISTS filestable(filestable TEXT,filetype TEXT,filesize TEXT,uploadDate TIMESTAMP)')


# Adding Details
def add_file_details(filename,filetype,filesize,uploadDate):
	c.execute('INSERT INTO filestable(filename,filetype,filesize,uploadDate) VALUES (?,?,?,?)',(filename,filetype,filesize,uploadDate))
	conn.commit()

# View Details
def view_all_data():
	c.execute('SELECT * FROM filestable')
	data = c.fetchall()
	return data

