import csv
import pymysql
import random

num = random.randint(0, 49)
conn = pymysql.connect(user='kirmada@kirmadabot', password='89800932Avi', host='kirmadabot.mysql.database.azure.com', database="botdata")
cur = conn.cursor()

# write
# with open('data.csv', 'r') as data_csv:
#     data = csv.reader(data_csv)
#
#     for lines in data:
#         cur.execute("INSERT INTO `acc` (`id`, `email`, `pass`) VALUES ('', '"+ lines[0] +"', '" + lines[1] +"');")

#read
cur.execute("SELECT `email` FROM `acc` WHERE id='5'")
da = cur.fetchone()
cur.execute("SELECT `pass` FROM `acc` WHERE id='5'")
pas = cur.fetchone()
print(da[-1])
print(pas[-1])

# cur.execute("CREATE TABLE `botdata`.`acc` ( `id` INT(200) NOT NULL AUTO_INCREMENT , `email` VARCHAR(200) NOT NULL , `pass` VARCHAR(200) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")

conn.commit()
cur.close()
conn.close()