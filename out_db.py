import sqlite3

# Replace 'your_database.db' with the path to your .db file
db_file = 'waf_comparison.db'
output_file = 'outputBlocked.txt'

# Connect to the database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Query the data
query = "SELECT * FROM waf_comparison WHERE isBlocked = 0"
cursor.execute(query)

# Fetch all rows and column names
rows = cursor.fetchall()
column_names = [description[0] for description in cursor.description]

# Write the results to a text file
with open(output_file, 'w') as f:
    # Write the column names as a header
    f.write(", ".join(column_names) + "\n")
    f.write("-" * 50 + "\n")  # Separator line
    
    # Write each row, formatting with column names
    for row in rows:
        row_dict = {column_names[i]: row[i] for i in range(len(column_names))}
        for key, value in row_dict.items():
            f.write(f"{key}: {value}\n")
        f.write("-" * 50 + "\n")  # Separator line between rows

# Close the database connection
conn.close()

print(f"Data extracted and written to {output_file}")