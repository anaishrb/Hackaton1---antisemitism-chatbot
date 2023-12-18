import curses
from multiprocessing import connection
import psycopg2

conn=psycopg2.connect(
    dbname='antisemitism_db',
    user='postgres',
    password='pgjav',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

def check_hate_speech(message):
    cur.execute("SELECT text_content FROM text_data WHERE text_content = %s AND label = 1", (message,))
    result = cur.fetchone()

    if result:
        return True, result[0]  # Hate speech detected, return associated text_content
    return False, None  # Not hate speech

def chatbot():
    print("Welcome to the Hate Speech Detector Chatbot!")
    while True:
        user_input = input("You: ")

        # Exit the chatbot if the user types 'exit'
        if user_input.lower() == 'exit':
            print("Chatbot: Bye! See you next time.")
            break

        # Check if the user input contains hate speech
        is_hate, non_hateful_response = check_hate_speech(user_input)

        # Provide appropriate response based on hate speech detection
        if is_hate:
            print("Chatbot: This content is hateful.")
            if non_hateful_response:
                print(f"Chatbot: The corresponding non-hateful content is - '{non_hateful_response}'")
        else:
            print("Chatbot: This content is appropriate.")

if __name__ == "__main__":
    chatbot()

# Close the cursor and connection
cur.close()
conn.close()