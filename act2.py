import os
import psycopg2
from flask import Flask
app = Flask(__name__)

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

@app.route('/<int:number>/')
def api(number):
    # Retorno de la temperatura media de todas las habitaciones.
    conn = get_db_conn()
    cur = conn.cursor()
    if (number == 1):
      try:
        cur.execute('SELECT AVG(temperature) AS avg_temp, room_id'
                    ' FROM temperatures GROUP BY(room_id) ORDER BY(avg_temp) DESC;')
      except (Exception, psycopg2.Error) as error :
        print ("Error while performing API #1: ", error)
        pass

      retValue = "Avg Temp\tRoom ID <br /> "
      for x in cur.fetchall():
        retValue += "{} \t {} <br /> ".format(round(x[0], 2), x[1])

      return retValue
    cur.close()
    conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

    
