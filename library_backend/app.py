from flask import Flask, jsonify, request

from flask_cors import CORS

from db_configure import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash
import smtplib
from email.mime.text import MIMEText


# -------------------------------
# APP INIT
# -------------------------------
app = Flask(__name__)
CORS(app)


# -------------------------------
# EMAIL FUNCTION
# -------------------------------
def send_email(to_email, subject, body):

    sender_email = "john@gmail.com"
    sender_password = "1234"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()

        print("Mail sent ✅")

    except Exception as e:
        print("Email error:", e)

# -------------------------------
# TEST ROUTE
# -------------------------------
@app.route("/")
def home():
    return "Library Backend Running ✅"

# -------------------------------
# USERS
# -------------------------------
@app.route("/users", methods=["GET"])
def get_users():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(users)

# -------------------------------
# REGISTER
# -------------------------------
@app.route("/register", methods=["POST"])
def register():

    try:
        data = request.json
        

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        phone = data.get("phone")
        password = data.get("password")
        student_id = data.get("student_id")

        if not all([first_name, last_name, email, phone, password]):
            return jsonify({"message": "Missing required fields"}), 400

        password_hash = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # ✅ CHECK IF EMAIL ALREADY EXISTS
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            return jsonify({"message": "Email already registered"}), 409

        # ✅ INSERT USER
        cursor.execute("""
            INSERT INTO users
            (first_name, last_name, email, phone, password_hash, student_id, role)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (
            first_name,
            last_name,
            email,
            phone,
            password_hash,
            student_id,
            "student"
        ))

        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({"message": "User registered successfully"}), 201

    except Exception as e:
        print("REGISTER ERROR:", e)
        return jsonify({"message": "Server error"}), 500


# -------------------------------
# LOGIN
# -------------------------------
@app.route("/login", methods=["POST"])
def login():

    data = request.json
    email = data["email"]
    password = data["password"]

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE email=%s",
        (email,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user and check_password_hash(user["password"], password):
        return jsonify({
            "message":"Login successful",
            "user_id":user["user_id"],
            "role":user["role"]
        })
    else:
        return jsonify({"message":"Invalid credentials"}),401

# -------------------------------
# BOOKS CRUD
# -------------------------------
@app.route("/books", methods=["GET"])
def get_books():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(books)

#Backend Route
@app.route("/books", methods=["POST"])
def add_book():

    data = request.json

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO books
    (title, author, isbn, category, copies, available, status,
     publisher, year, pages, language, location, callNumber,
     description, tags, image)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        data.get("title"),
        data.get("author"),
        data.get("isbn"),
        data.get("category"),
        data.get("copies"),
        data.get("available"),
        data.get("status"),
        data.get("publisher"),
        data.get("year"),
        data.get("pages"),
        data.get("language"),
        data.get("location"),
        data.get("callNumber"),
        data.get("description"),
        data.get("tags"),
        data.get("image")
    )

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Book added successfully"})


#Backend API Route
@app.route("/books/<int:book_id>", methods=["GET"])
def get_single_book(book_id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM books WHERE id=%s",
        (book_id,)
    )

    book = cursor.fetchone()

    cursor.close()
    conn.close()

    if book:
        return jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404




# UPDATE BOOK
@app.route("/update_book/<int:book_id>", methods=["PUT"])
def update_book(book_id):

    data = request.json

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE books
        SET title=%s,author=%s,genre=%s,
            isbn=%s,availability=%s
        WHERE book_id=%s
    """, (
        data["title"],
        data["author"],
        data["genre"],
        data["isbn"],
        data["availability"],
        book_id
    ))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message":"Book updated successfully"})

# DELETE BOOK
@app.route("/delete_book/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM books WHERE book_id=%s",
        (book_id,)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message":"Book deleted successfully"})

# SEARCH
@app.route("/search_books", methods=["GET"])
def search_books():

    title = request.args.get("title")

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM books
        WHERE title LIKE %s
    """, ("%"+title+"%",))

    books = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(books)

# -------------------------------
# ISSUE BOOK
# -------------------------------
@app.route("/issue_book", methods=["POST"])
def issue_book():

    data = request.json

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO transactions
        (user_id,book_id,issue_date,return_date,status)
        VALUES (%s,%s,%s,%s,'issued')
    """, (
        data["user_id"],
        data["book_id"],
        data["issue_date"],
        data["return_date"]
    ))

    cursor.execute(
        "UPDATE books SET availability='issued' WHERE book_id=%s",
        (data["book_id"],)
    )

    conn.commit()

    # EMAIL
    cursor.execute(
        "SELECT email FROM users WHERE user_id=%s",
        (data["user_id"],)
    )
    email = cursor.fetchone()[0]

    send_email(
        email,
        "Book Issued",
        f"Book ID {data['book_id']} issued successfully. Return before {data['return_date']}."
    )

    cursor.close()
    conn.close()

    return jsonify({"message":"Book issued successfully"})

# -------------------------------
# RETURN BOOK
# -------------------------------
@app.route("/return_book/<int:transaction_id>", methods=["PUT"])
def return_book(transaction_id):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE transactions SET status='returned' WHERE transaction_id=%s",
        (transaction_id,)
    )

    cursor.execute(
        "SELECT book_id,user_id FROM transactions WHERE transaction_id=%s",
        (transaction_id,)
    )
    data = cursor.fetchone()
    book_id = data[0]
    user_id = data[1]

    cursor.execute(
        "UPDATE books SET availability='available' WHERE book_id=%s",
        (book_id,)
    )

    conn.commit()

    # EMAIL
    cursor.execute(
        "SELECT email FROM users WHERE user_id=%s",
        (user_id,)
    )
    email = cursor.fetchone()[0]

    send_email(
        email,
        "Book Returned",
        f"Book ID {book_id} returned successfully."
    )

    cursor.close()
    conn.close()

    return jsonify({"message":"Book returned successfully"})

# -------------------------------
# USER HISTORY
# -------------------------------
@app.route("/user_history/<int:user_id>")
def user_history(user_id):

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT t.transaction_id,b.title,
               t.issue_date,t.return_date,t.status
        FROM transactions t
        JOIN books b ON t.book_id=b.book_id
        WHERE t.user_id=%s
    """,(user_id,))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)

# -------------------------------
# OVERDUE
# -------------------------------
@app.route("/overdue_books")
def overdue_books():

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT u.name,b.title,
               t.issue_date,t.return_date
        FROM transactions t
        JOIN users u ON t.user_id=u.user_id
        JOIN books b ON t.book_id=b.book_id
        WHERE t.status='issued'
        AND t.return_date<CURDATE()
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)

# -------------------------------
# ANALYTICS
# -------------------------------
@app.route("/analytics/total_books")
def total_books():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM books")
    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return jsonify({"total_books":count})

@app.route("/analytics/issued_books")
def issued_books():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM books WHERE availability='issued'"
    )
    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return jsonify({"issued_books":count})

@app.route("/analytics/overdue_count")
def overdue_count():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*) FROM transactions
        WHERE status='issued'
        AND return_date<CURDATE()
    """)
    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return jsonify({"overdue_books":count})

@app.route("/analytics/total_users")
def total_users():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return jsonify({"total_users":count})

# -------------------------------
# RUN SERVER
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)


