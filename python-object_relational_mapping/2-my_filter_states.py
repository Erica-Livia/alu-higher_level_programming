#!/usr/bin/python3
"""list states from databased"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name = '{}' OREDER BY\
    states.id ASC".format(argv[4]))
    result = cur.fetchall()
    for i in result:
        if i[1] == argv[4]:
            print(i)
    cur.close()
    db.close()
