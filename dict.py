import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="database",
   user="user",
   password="abc123"
)

def read_dict(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_word(conn, word, translation):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def delete_word(conn, ID):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
def save_dict(conn):
    cur = conn.cursor()
    cur.execute("COMMIT;")
    cur.close()
## some more

def main():
    while True: ## REPL - Read Execute Program Loop
        cmd = input("Command: ")
        if cmd == "LIST":
            print(read_dict(conn))
        elif cmd == "ADD":
            name = input("  Word: ")
            phone = input("  Translation: ")
            add_word(conn, name, phone)
        elif cmd == "DELETE":
            ID = input("  ID: ")
            delete_word(conn, ID)
        elif cmd == "QUIT":
            save_dict(conn)
            exit()


main()
# some comments
