import tkinter as tk
from tkinter import messagebox
import subprocess

class SignalSchedulerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Signal Message Scheduler | Made by ASTRAL")
        self.root.geometry("820x640")
        self.root.configure(bg="black")  # Set background to black

        # Common font and color settings
        font = ("Courier", 12)
        fg_color = "lime"
        bg_color = "black"

        # Title Label
        self.title_label = tk.Label(root, text="Signal Message Scheduler", font=("Courier", 18, "bold"),
                                    fg=fg_color, bg=bg_color)
        self.title_label.pack(pady=20)

        # User's Signal Phone Number
        self.phone_number_label = tk.Label(root, text="Your Signal Phone Number:", font=font,
                                           fg=fg_color, bg=bg_color)
        self.phone_number_label.pack(pady=10)
        self.phone_number_entry = tk.Entry(root, width=40, font=font, fg=fg_color, bg=bg_color, insertbackground=fg_color)
        self.phone_number_entry.pack(pady=5)

        # Recipient Phone Number
        self.recipient_label = tk.Label(root, text="Recipient's Phone Number:", font=font,
                                        fg=fg_color, bg=bg_color)
        self.recipient_label.pack(pady=10)
        self.recipient_entry = tk.Entry(root, width=40, font=font, fg=fg_color, bg=bg_color, insertbackground=fg_color)
        self.recipient_entry.pack(pady=5)

        # Message Text
        self.message_label = tk.Label(root, text="Enter Your Message:", font=font,
                                      fg=fg_color, bg=bg_color)
        self.message_label.pack(pady=10)
        self.message_text = tk.Text(root, height=6, width=60, font=font, fg=fg_color, bg=bg_color, insertbackground=fg_color)
        self.message_text.pack(pady=5)

        # Schedule Time
        self.time_label = tk.Label(root, text="Schedule Time (e.g., 06:59 AM 03/27/2025):", font=font,
                                   fg=fg_color, bg=bg_color)
        self.time_label.pack(pady=10)
        self.time_entry = tk.Entry(root, width=30, font=font, fg=fg_color, bg=bg_color, insertbackground=fg_color)
        self.time_entry.pack(pady=5)

        # Schedule Button
        self.schedule_button = tk.Button(root, text="Schedule Message", font=font,
                                         fg=fg_color, bg="#222", command=self.schedule_message)
        self.schedule_button.pack(pady=20)

    def schedule_message(self):
        user_phone_number = self.phone_number_entry.get()
        recipient = self.recipient_entry.get()
        message = self.message_text.get("1.0", tk.END).strip()
        schedule_time = self.time_entry.get()

        if not user_phone_number or not recipient or not message or not schedule_time:
            messagebox.showwarning("Input Error", "Please enter all fields.")
            return

        signal_command = f'signal-cli -u {user_phone_number} send -m "{message}" {recipient}'
        full_command = f"echo '{signal_command}' | at {schedule_time}"

        try:
            subprocess.run(full_command, shell=True, check=True)
            messagebox.showinfo("Scheduled", f"Message scheduled for {schedule_time}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to schedule message: {str(e)}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SignalSchedulerGUI(root)
    root.mainloop()
