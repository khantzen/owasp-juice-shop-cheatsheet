
print("From https://www.techonthenet.com/sqlite/sys_tables/index.php")

print("""
SQLite: System Tables

SQLite databases have a set of system tables (ie: catalog tables). You can easily identify a system table in SQLite because the table name will start with the sqlite_ prefix.

SQLite system tables can be queried in the database using a SELECT statement just like any other table.

Below is a listing of the SQLite system tables that are commonly used.

+------------------------------------------------------------------------------------------------------------------------------
+ sqlite_master   + Master listing of all database objects in the database and the SQL used to create each object.
------------------+-------------------------------------------------------------------------------------------------------------
+                 + Lists the last sequence number used for the AUTOINCREMENT column in a table.
+ sqlite_sequence +               + The sqlite_sequence table will only be created once an AUTOINCREMENT column has been defined in the database 
+                 + and at least one sequence number value has been generated and used in the database.
+-----------------+--------------------------------------------------------------------------------------------------------------
+                 +
+ sqlite_stat1 	  + This table is created by the ANALYZE command to store statistical information about the tables and indexes analyzed. 
+                 + This information will be later used by the query optimizer.
+                 +
------------------+--------------------------------------------------------------------------------------------------------------
""")

print("""
1. sqlite_master

The sqlite_master table contains the following columns:

+--------------+---------------
+ Column Name  + Description 
+--------------+---------------
+ type         + The type of database object such as table, index, trigger or view.
+--------------+---------------
+ name         + The name of the database object.
+--------------+---------------
+ tbl_name     + The table name that the database object is associated with.
+--------------+---------------
+ rootpage     + Root page.
+--------------+---------------
+ sql          + SQL used to create the database object.
+--------------+---------------
""")

