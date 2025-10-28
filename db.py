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
    base_cols = ["ID INTEGER PRIMARY KEY AUTOINCREMENT", "name TEXT", "created_at TEXT"]
    cols_str = ", ".join(base_cols + list(cols))

    con, cur = getcur(db_name)
    cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({cols_str})")
    con.commit()
    con.close()

def inserttotable(db_name, table_name, values_list, cols=None):
    con, cur = getcur(db_name)

    if cols is None:
        cur.execute(f"PRAGMA table_info({table_name})")
        cols = [row[1] for row in cur.fetchall()]

    # Ensure values are a list of tuples
    if isinstance(values_list[0], (str, int, float)):
        values_list = [tuple(values_list)]

    for row in values_list:
        if len(row) != len(cols):
            raise ValueError(f"Expected {len(cols)} values, got {len(row)}")

    placeholders = ", ".join(["?"] * len(cols))
    cols_str = ", ".join(cols)
    sql = f"INSERT INTO {table_name} ({cols_str}) VALUES ({placeholders})"
    cur.executemany(sql, values_list)
    con.commit()
    con.close()

def getfromdb(db_name, table_name, place, place_value, time, time_value):
    con, cur = getcur(db_name)
    sql = f"SELECT ID FROM {table_name} WHERE {place} = ? AND {time} = ?"
    cur.execute(sql, (place_value, time_value))
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