import psycopg2
from ..const import sql

def executeQuery(query):
    conn = psycopg2.connect(sql.SQLCONNECT)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    pass

def executeQueryTupple(query,var):
    conn = psycopg2.connect(sql.SQLCONNECT)
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()
    cur.close()
    conn.close()

def selectOneQueryTupple(query,var):
    conn = psycopg2.connect(sql.SQLCONNECT)
    cur = conn.cursor()
    cur.execute(query,var)
    getOne = cur.fetchone()
    cur.close()
    conn.close()
    return getOne

def selectAllQuery(query):
    conn = psycopg2.connect(sql.SQLCONNECT)
    cur = conn.cursor()
    cur.execute(query)
    getAll = cur.fetchall()
    cur.close()
    conn.close()
    return getAll

def selectAllQueryTupple(query,var):
    conn = psycopg2.connect(sql.SQLCONNECT)
    cur = conn.cursor()
    cur.execute(query,var)
    getAll = cur.fetchall()
    cur.close()
    conn.close()
    return getAll

def getConnection():
    return psycopg2.connect(sql.SQLCONNECT)

