import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# # Configure MySQL from environment variables
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'default_user')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'default_password')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'default_db')

# Initialize MySQL
mysql = MySQL(app)

# def init_db():
#     with app.app_context():
#         cur = mysql.connection.cursor()
#         cur.execute('''
#         CREATE TABLE IF NOT EXISTS messages (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             message TEXT
#         );
#         ''')
#         mysql.connection.commit()  
#         cur.close()


def init_db():
    """Automatically create database and table if they don't exist"""
    try:
        # Step 1: Connect WITHOUT selecting a database
        conn = MySQLdb.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            passwd=app.config['MYSQL_PASSWORD']
        )
        cursor = conn.cursor()
        
        # Step 2: Create database if it doesn't exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {app.config['MYSQL_DB']}")
        cursor.close()
        conn.close()
        print(f"✅ Database '{app.config['MYSQL_DB']}' is ready")
        
        # Step 3: Now connect to the database and create table
        with app.app_context():
            cur = mysql.connection.cursor()
            cur.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INT AUTO_INCREMENT PRIMARY KEY,
                message TEXT
            );
            ''')
            mysql.connection.commit()
            cur.close()
            print("✅ Table 'messages' is ready")
            
    except Exception as e:
        print(f"❌ Database initialization error: {e}")
        raise


@app.route('/')
def hello():
    cur = mysql.connection.cursor()
    cur.execute('SELECT message FROM messages')
    messages = cur.fetchall()
    cur.close()
    return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit():
    new_message = request.form.get('new_message')
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO messages (message) VALUES (%s)', [new_message])
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': new_message})

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

