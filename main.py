from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Configure database connection details
db_host = "plimsoltech"
db_name = "meal-treat.db"
db_user = "plimsoltech"
db_password = "plimsoltech"

# Define the route for the contact form
@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Connect to the database
        conn = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=db_password)
        cur = conn.cursor()

        # Insert form data into the database
        cur.execute("INSERT INTO contact_form (name, email, message) VALUES (%s, %s, %s)",
                    (name, email, message))
        conn.commit()

        # Close the database connection
        cur.close()
        conn.close()

        return 'Form submitted successfully!'

    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
