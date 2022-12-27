import os
import psycopg2
from flask import Flask
from flask import request
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


    elif (number == 2):
      try:
        cur.execute('SELECT MAX(temperature) AS max_temp, room_id'
                    ' FROM temperatures GROUP BY(room_id) ORDER BY(max_temp) DESC;')
      except (Exception, psycopg2.Error) as error :
        print ("Error while performing API #2: ", error)
        pass

      retValue = "Max Temp\tRoom ID <br /> "
      for x in cur.fetchall():
        retValue += "{} \t {} <br /> ".format(round(x[0], 2), x[1])

      return retValue


    elif (number == 3):
      id = request.args.get('id', type = int)
      try:
        cur.execute('SELECT name FROM rooms WHERE id = %s;',
                    (id, )
                   )
      except (Exception, psycopg2.Error) as error :
        print ("Error while performing API #3: ", error)
        pass

      retValue = "Room Name <br /> "
      for x in cur.fetchall():
        retValue += "{} <br /> ".format(x[0])

      return retValue
    cur.close()
    conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

    
