import sqlite3
con3 = sqlite3.connect("chefprofile.db")

con3.execute("ATTACH 'waiterprofile.db' as dba")

con3.execute("BEGIN")
for row in con3.execute("SELECT * FROM dba.sqlite_master WHERE type='table'"):
    combine = "INSERT INTO "+ row[1] + " SELECT * FROM dba." + row[1]
    print(combine)
    con3.execute(combine)
con3.commit()
con3.execute("detach database dba")