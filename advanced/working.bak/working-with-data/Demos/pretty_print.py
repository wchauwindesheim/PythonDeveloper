# Be sure to install via pip install mysql-connector-python
import mysql.connector
from pprint import pprint

connection = mysql.connector.connect(
    host='oraculo.nl',
    user='u10962p7733_python',
    passwd='zyZBOD8mCFGlqyAd',
    db='u10962p7733_lahmansbaseballdb'
)

query = """SELECT nameFirst, nameLast, weight, year(debut)
           FROM people
           ORDER BY weight DESC
           LIMIT 5"""

cursor = connection.cursor(dictionary=True)
cursor.execute(query)
results = cursor.fetchall()

cursor.close()
connection.close()

pprint(results)