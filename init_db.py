import os
import psycopg2
try:
    conn = psycopg2.connect(
                host="localhost",
                database="prueba",
                #user=os.environ['DB_USERNAME'],
                #password=os.environ['DB_PASSWORD']
                user='postgres',
                password='postgres')

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute('DROP TABLE IF EXISTS books;')
    try:
        cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                        'title varchar (150) NOT NULL,'
                                        'author varchar (50) NOT NULL,'
                                        'pages_num integer NOT NULL,'
                                        'review text,'
                                        'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                        )
    except (Exception, psycopg2.Error) as error :
        print ("Error while creating the table: ", error)

    # Insert data into the table
    try: 
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)',
                    ('Anna Karenina',
                    'Leo Tolstoy',
                    864,
                    'Another great classic!')
                    )
    except (Exception, psycopg2.Error) as error :
        print ("Error while inserting a book 1: ", error)
        pass

    try:
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('To Kill a Mockingbird',
                'Harper Lee',
                336,
                'A novel of strong contemporary national significance.')
                )
    except (Exception, psycopg2.Error) as error :
        print ("Error while inserting a book 2: ", error)
        pass

    try:
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('Where the Sidewalk Ends',
                'Shel Silverstein',
                176,
                'A zesty collection of humorous light verse.')
                )
    except (Exception, psycopg2.Error) as error :
        print ("Error while inserting a book 3: ", error)
        pass

    try:
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('Mortadelo y Filemón',
                'Ibáñez',
                50,
                'Clásico del cómic español.')
                )
    except (Exception, psycopg2.Error) as error :
        print ("Error while inserting a book 4: ", error)
        pass

    try:
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('Marina',
                'Carlos Ruiz Zafón',
                150,
                'Está escrito de una forma increíble, la forma de narrar de Ruiz Zafón es muy elegante.')
                )
    except (Exception, psycopg2.Error) as error :
        print ("Error while inserting a book 5: ", error)
        pass

    try:
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('HARRY POTTER Y LA PIEDRA FILOSOFAL',
                'J. K. Rowling',
                254,
                ' Gran novela de fantasía juvenil.')
                )
    except (Exception, psycopg2.Error) as error :
        print ("Error while inserting a book 6: ", error)
        pass

    try:
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('El día que se perdió la cordura',
                'Javier Castillo',
                194,
                'La palabra que mejor pudiese definir mejor a la novela es “tensión”.')
                )
    except (Exception, psycopg2.Error) as error :
        print ("Error while inserting a book 7: ", error)
        pass

    try:
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('El enigma de la habitación 622 ',
                'J. Dicker',
                342,
                'es una comedia de enredo con máscara de thriller, modelo de literatura muy atrayente por unir dos géneros, ambos por sí solos, ya muy leídos.')
                )
    except (Exception, psycopg2.Error) as error :
        print ("Error while inserting a book 8: ", error)
        pass

    try:
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('El libro del sepulturero',
                'Olvier Pötzsch',
                231,
                'Es una buena novela policíaca')
                )
    except (Exception, psycopg2.Error) as error :
        print ("Error while inserting a book 9: ", error)
        pass

    conn.commit()

    cur.close()
    conn.close()
    
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL: ", error)