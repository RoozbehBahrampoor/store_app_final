import sqlite3


def create_database():

    connection = sqlite3.connect("store.db.sqlite")

    cursor = connection.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS ADMINS
                   (
                       code     integer primary key,
                       name     text not null,
                       family   text not null,
                       email    text not null,
                       username text not null unique,
                       password text not null,
                       locked   tinyint default 0
                   )
                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Customers
                   (
                       code         integer primary key,
                       name         text not null,
                       family       text not null,
                       email        text not null,
                       username     text not null unique,
                       password     text not null,
                       phone_number text
                   )
                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS Cars
                   (
                       code   integer primary key,
                       name   text    not null,
                       model  text    not null,
                       color  text    not null,
                       year   integer not null unique,
                       price  integer not null,
                       locked tinyint default 0
                   )
                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS House
                   (
                       code      integer primary key,
                       region    text    not null,
                       address   text    not null,
                       floor     text    not null,
                       area      text    not null unique,
                       rooms     text    not null,
                       elevators text    not null,
                       parking   text    not null,
                       storage   text    not null,
                       year      integer not null unique,
                       price     integer not null,
                       locked    tinyint default 0
                   )
                   """)

    connection.commit()

    cursor.close()
    connection.close()
