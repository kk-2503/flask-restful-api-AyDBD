import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="prueba",
        #user=os.environ['DB_USERNAME'],
        #password=os.environ['DB_PASSWORD']
		user='postgres',
        password='postgres')
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute('SELECT * FROM books;')
    except psycopg2.Error as err:
        print(err)
        pass
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = int(request.form['pages_num'])
        review = request.form['review']

        try:
            conn = get_db_connection()
        except psycopg2.Error as e:
            pass
        try:
            cur = conn.cursor()
            cur.execute('INSERT INTO books (title, author, pages_num, review)'
                        'VALUES (%s, %s, %s, %s)',
                        (title, author, pages_num, review))
        except psycopg2.Error as e:
            pass
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/delete/', methods=('GET', 'POST'))
def delete():
    if request.method == 'POST':
        id = int(request.form['id'])

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM books'
                    ' WHERE id=%s',
                    (id, ))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('delete.html')

@app.route('/update/', methods=('GET', 'POST'))
def update():
    if request.method == 'POST':
        id = int(request.form['id'])
        title = request.form['title']
        author = request.form['author']
        pages_num = int(request.form['pages_num'])
        review = request.form['review']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE books'
                    ' SET title = %s, author = %s, pages_num = %s, review = %s'
                    ' WHERE id=%s',
                    (title, author, pages_num, review, id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('update.html')


@app.route('/about/')
def about():
    return render_template('about.html')
