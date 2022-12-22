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
    # cur.execute('DROP TABLE IF EXISTS books;')
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
        print ("Error while inserting a book: ", error)
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
        print ("Error while inserting a book: ", error)
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
        print ("Error while inserting a book: ", error)
        pass

    conn.commit()

    cur.close()
    conn.close()
    
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL: ", error)