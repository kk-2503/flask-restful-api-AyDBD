import os
import psycopg2

def get_db_conn():
  try:
      conn = psycopg2.connect(
                  host="localhost",
                  database="myhome",
                  #user=os.environ['DB_USERNAME'],
                  #password=os.environ['DB_PASSWORD']
                  user='postgres',
                  password='postgres')
      return conn    
  except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL: ", error)

def api1():
    # Retorno de la temperatura media de todas las habitaciones.
    conn = get_db_conn()
    cur = conn.cursor()
    try:
      cur.execute('SELECT AVG(temperature) AS avg_temp, room_id'
                  ' FROM temperatures GROUP BY(room_id) ORDER BY(avg_temp) DESC;')
    except (Exception, psycopg2.Error) as error :
      print ("Error while performing API #1: ", error)
      pass

    print("Avg Temp\tRoom ID")
    for x in cur.fetchall():
      print("{} \t {}".format(round(x[0], 2), x[1]))
    cur.close()
    conn.close()

api1()
    
