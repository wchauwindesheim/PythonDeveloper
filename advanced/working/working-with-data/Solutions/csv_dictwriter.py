import mysql.connector
import csv

connection = mysql.connector.connect(
    host='oraculo.nl',
    user='u10962p7733_python',
    passwd='zyZBOD8mCFGlqyAd',
    db='u10962p7733_lahmansbaseballdb'
)

query = """SELECT year(debut) AS year, avg(weight) AS weight
FROM people
WHERE debut is NOT NULL
GROUP BY year(debut)
ORDER BY year(debut)"""

cursor = connection.cursor(dictionary=True)
cursor.execute(query)
results = cursor.fetchall()

cursor.close()
connection.close()

csv_file = '../data/mlb-weight-over-time.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = results[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)