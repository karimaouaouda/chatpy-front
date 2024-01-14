import tkinter as tk
import openai

API_KEY = "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"
openai.api_key = API_KEY


def send_message(event=None):
    global root
    user_message = user_input.get()
    message = tk.Text(chat_log, bg="#17202A", fg="#EAECEE", font="Helvetica 14", height=20, width=150)
    message.insert(tk.END, user_message)
    message.pack()

    if user_message.lower() == "quit":
        root.destroy()
    else:
        chat_log.insert(tk.END, "ChatGPT: " + generate_response(user_message) + "\n")
        user_input.delete(0, tk.END)


def generate_response(event=None):
    global root
    user_message = user_input.get()
    message = tk.Text(root, bg="#17202A", fg="#EAECEE", font="Helvetica 14")
    message.insert(tk.END, user_message)
    message.pack()

    if user_message.lower() == "quit":
        root.destroy()
    else:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        assistant_response = response['choices'][0]['message']['content']
        chat_log.insert(tk.END, "ChatGPT: " + assistant_response.strip() + "\n")

        user_input.delete(0, tk.END)
        chat_log.see(tk.END)


root = tk.Tk()
root.title("Chat Interface")

chat_log = tk.Frame(root, height=200, width=200)
chat_log.pack()

user_input = tk.Entry(root, bg="#2C3E50", fg="#EAECEE", font="Helvetica 14", width=55)
user_input.pack()
user_input.focus_set()

send_button = tk.Button(root, text="Send", font="Helvetica 13 bold", bg="#ABB2B9", command=generate_response)
send_button.pack()

root.bind('<Return>', generate_response)

root.mainloop()
