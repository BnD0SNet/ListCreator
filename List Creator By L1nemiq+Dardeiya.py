import os
import sys
sys_key = ".AccessKey"
import threading
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from tkinter import scrolledtext


n = 0
i = 0
current_log = ""
data_list = []
subscription = 0  # 0 - Basic subscription, 1 - Pro+ subscription

print("Welcome to the list creation program!!")

def Subscribe():
    global n
    global data_list
    global i
    while i < n:
        user_string = input(f"Enter item #{i + 1} that you want to add: ")
        
        if user_string.strip() != "":
            if user_string == "/stop":
                break
            else:
                data_list.append(user_string)
                i += 1
        else:
            print("\nError: Item cannot be empty! Please try again.")
        print("\nYou can also stop the process and display the list immediately! Command: /stop")

    print("\nYou have created a list!\n")
    print(data_list)

def DefaultSubscribe():
    global n
    while n == 0:
        try:
            n = int(input("Enter the number of items: "))
            if n > 10:
                print("\nAccess denied! You cannot enter more than 10 items!")
                print("Please purchase the Pro+ subscription.\n")
                n = 0
        except ValueError:
            print("Text and special characters are not allowed! Please enter a valid number.")
    Subscribe()
    print("\nTo create a larger list, \npurchase a subscription from the developer of this mini-project @L1nemiq\n")
    if data_list == []:
        print("\nThe list is empty! Create a new one by running the program again.")
    else:
        pass

def ProSubscribe():
    global n
    while n == 0:
        try:
            n = int(input("Enter the number of items: "))
        except ValueError:
            print("Text and special characters are not allowed! Please enter a valid number.")
    Subscribe()
    print("\nSubscription detected! \nThank you for using the program and for your support!\n")
    if data_list == []:
        print("\nThe list is empty! Create a new one by running the program again.")
    else:
        pass

def DardeiyaSubscribe():
    window = tk.Tk()
    window.title("Subscribe Dardeiya+")
    window.geometry("900x650")
    window.config(bg="#2A3A35")

    def OnType(*args):
        global current_log
        chat_history.config(state=tk.NORMAL)
        chat_history.delete("1.0", tk.END)
        chat_history.insert(tk.END, current_log)
        chat_history.insert(tk.END, f"Enter item #{i + 1} that you want to add: {input_tracker.get()}")
        chat_history.see(tk.END)
        chat_history.config(state=tk.DISABLED)


    def ListCreator(command):
        global data_list
        global i
        global current_log
        
        if command == "/stop":
            os._exit(0)
        elif command == "/clear":
            data_list.clear()
            current_log = ""
            i = 0
            OnType()
        else:
            data_list.append(command)
            current_log += f"Enter item #{i + 1} that you want to add: {command}\n"
            i += 1
            OnType()

    def SendMessage(event=None):
        command = user_input.get()
        Creating = threading.Thread(target=ListCreator, args=(command,))
        Creating.start()
        user_input.delete(0, tk.END)

    def SendList():
        if data_list == []:
            messagebox.showinfo("List", "The list is empty!")
        else:
            formatted_lines = []
            for num, item in enumerate(data_list, start=1):
                formatted_lines.append(f"{num}. {item}")
            
            final_text = "\n".join(formatted_lines)
            
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_name = f"list_{current_time}.txt"
            
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(final_text)
                
            messagebox.showinfo("List", f"Saved to {file_name}\n\n{final_text}")



    chat_history = scrolledtext.ScrolledText(window, width=80, height=30)
    chat_history.config(state=tk.DISABLED, bg="#EAF2EE", fg="#1D2622", font=("Helvetica", 10, "bold italic"))
    chat_history.pack(pady=10)

    input_tracker = tk.StringVar()
    input_tracker.trace_add("write", OnType)

    user_input = tk.Entry(window, textvariable=input_tracker)
    user_input.config(bg="#EAF2EE", width=80, fg="#1D2622", font=("Helvetica", 10, "bold italic"))
    user_input.focus()
    user_input.pack(pady=15)

    commands_info = tk.Label(window, text="COMMANDS:\n\n/clear — Clear\n/stop — Exit", bg="#2A3A35", fg="#B6DDBE", font=("Arial", 10, "bold"), justify=tk.LEFT)
    commands_info.place(x=20, y=250) 

    send_button = tk.Button(window, text="➤", command=SendMessage)
    send_button.config(bg="#3B6B55", fg="#B6DDBE", font=("Arial", 10, "bold"), width=10)
    send_button.pack(pady=10)

    end_button = tk.Button(window, text="< Show and Save List >", command=SendList)
    end_button.config(bg="#4A76A8", fg="#B6DDBE", font=("Arial", 10, "bold"), width=50)
    end_button.pack(pady=15)

    OnType()
    window.bind('<Return>', SendMessage)
    window.mainloop()

if os.path.exists(sys_key) or subscription == "Dardeiya":
    DardeiyaSubscribe()
elif subscription == 0:
    print("Subscription: Basic, up to 10 items per list\n")
    DefaultSubscribe()
elif subscription == 1:
    print("Subscription: Pro+, unlimited items per list\n")
    ProSubscribe()
else:
    print("Unknown program signature.")
    messagebox.showerror("Error", "Unknown program signature.")
