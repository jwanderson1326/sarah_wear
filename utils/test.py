from db_functions import *

db = connect_to_db()

curs = db.cursor()
query = format_schema_query({'temperature':'INT', 'clothes': 'varchar(30)'}, 'temperature','clothes')
print(query)
curs.execute(query)

curs.close()

