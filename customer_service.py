import sqlite3
import csv

conn = sqlite3.connect('customer_reviews.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS reviews (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 first_name TEXT NOT NULL,
                 last_name TEXT NOT NULL,
                 rating INTEGER NOT NULL,
                 reason TEXT NOT NULL
             )''')

def add_review(first_name, last_name, rating, reason):
    with conn:
        c.execute("INSERT INTO reviews (first_name, last_name, rating, reason) VALUES (?, ?, ?, ?)",
                  (first_name, last_name, rating, reason))

def display_reviews():
    c.execute("SELECT * FROM reviews")
    reviews = c.fetchall()
    for review in reviews:
        print(review)

def export_reviews_to_csv(filename):
    c.execute("SELECT * FROM reviews")
    reviews = c.fetchall()
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['ID', 'First Name', 'Last Name', 'Rating', 'Reason'])  # Write headers
        csvwriter.writerows(reviews)  # Write data


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
rating = int(input("Enter your rating (1-5): "))
reason = input("Enter the reason for your rating: ")

add_review(first_name, last_name, rating, reason)

print("\nAll Reviews:")
display_reviews()

csv_filename = 'customer_reviews.csv'
export_reviews_to_csv(csv_filename)
print(f"\nReviews have been exported to {csv_filename}")

conn.close()