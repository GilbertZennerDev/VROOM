import streamlit as st
import sqlite3 as s
import random as r
import sys

def getcon(name):
    return s.connect(name)

def getcur(name):
    con = getcon(name)
    return con, con.cursor()

def gendb(name='db.db'):
    getcon(name).close()

def addtable(db_name, table_name, *cols):
    cols_str = ", ".join(cols)
    con, cur = getcur(db_name)
    cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name}({cols_str})")
    con.commit()
    con.close()

def inserttotable(db_name, table_name, values_list):
    con, cur = getcur(db_name)
    cur.execute(f"PRAGMA table_info({table_name})")
    cols = [row[1] for row in cur.fetchall()]  # row[1] is column table_name

    # Ensure values are a list of tuples
    if isinstance(values_list[0], (str, int, float)):
        values_list = [tuple(values_list)]  # single row

         # Check that each row matches column count
    for row in values_list:
        if len(row) != len(cols):
            raise ValueError(f"Expected {len(cols)} values, got {len(row)}")

    # Use executemany for efficiency
    placeholders = ", ".join(["?"] * len(cols))
    sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
    cur.executemany(sql, values_list)
    con.commit()
    con.close()

def getfromdb(db_name, table_name, value_name, value):
    con, cur = getcur(db_name)
    cur.execute(f"PRAGMA table_info({table_name})")
    cols = [row[1] for row in cur.fetchall()]  # row[1] is column table_name
    sql = f"SELECT ID FROM {table_name} WHERE {value_name} = ?"
    cur.execute(sql, (value,))
    result = cur.fetchall()
    con.close()
    return result

def gendummypeople(size):
    people = []
    for i in range(size):
        name = "".join([chr(r.randint(97, 97+26)) for j in range(5)])
        age = r.randint(18, 60)
        people.append((name, age))
    inserttotable("people", people)

if __name__ == '__main__':
    pass
#addtable("people", "name", "age")
#inserttotable("people", [("Alice", 30), ("Thomas", 30)])
#gendummypeople(20)