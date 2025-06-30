import tkinter as tk
from tkinter import scrolledtext
from ollama import Client
import threading

client = Client(host='http://localhost:11434')

def get_emergency_response(user_input, result_display):
    prompt = f"You are an offline emergency assistant. Answer clearly and helpfully.\nUser: {user_input}\nAssistant:"
    
    try:
        # Show that the assistant is thinking
        result_display.config(state='normal')
        result_display.insert(tk.END, "\nAssistant: Thinking...\n")
        result_display.see(tk.END)
        result_display.config(state='disabled')

        # Call Ollama model (Gemma 2B)
        response = client.chat(
            model='gemma:2b',
            messages=[{"role": "user", "content": prompt}]
        )
        message = response['message']['content'].strip()

        # Display the response
        result_display.config(state='normal')
        result_display.insert(tk.END, f"{message}\n\n")
        result_display.see(tk.END)
        result_display.config(state='disabled')

    except Exception as e:
        result_display.config(state='normal')
        result_display.insert(tk.END, f"\n[Error: {e}]\n")
        result_display.config(state='disabled')

def on_ask_click(entry, result_display):
    user_input = entry.get()
    if user_input.strip() == "":
        return
    result_display.config(state='normal')
    result_display.insert(tk.END, f"\nUser: {user_input}\n")
    result_display.config(state='disabled')
    entry.delete(0, tk.END)

    # Run the response function in a new thread
    threading.Thread(target=get_emergency_response, args=(user_input, result_display), daemon=True).start()

def create_app():
    window = tk.Tk()
    window.title("Gemma Emergency Assistant")
    window.geometry("600x500")

    label = tk.Label(window, text="Ask your emergency question:")
    label.pack(pady=10)

    entry = tk.Entry(window, width=80)
    entry.pack(pady=5)

    ask_button = tk.Button(window, text="Get Help", command=lambda: on_ask_click(entry, result_display))
    ask_button.pack(pady=5)

    result_display = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=20, state='disabled')
    result_display.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_app()
