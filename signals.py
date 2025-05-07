import tkinter as tk
from tkinter import messagebox
import subprocess

class SignalSchedulerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Signal Message Scheduler")
        self.root.geometry("820x640")
        
        # Title Label
        self.title_label = tk.Label(root, text="Signal Message Scheduler", font=("Helvetica", 18, "bold"), bg="lightblue")
        self.title_label.pack(pady=20)
        
        # User's Signal Phone Number
        self.phone_number_label = tk.Label(root, text="Your Signal Phone Number:", font=("Helvetica", 12), bg="lightblue")
        self.phone_number_label.pack(pady=10)
        self.phone_number_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
        self.phone_number_entry.pack(pady=5)

        # Recipient Phone Number
        self.recipient_label = tk.Label(root, text="Recipient's Phone Number:", font=("Helvetica", 12), bg="lightblue")
        self.recipient_label.pack(pady=10)
        self.recipient_entry = tk.Entry(root, width=40, font=("Helvetica", 12))
        self.recipient_entry.pack(pady=5)

        # Message Text (Larger Field)
        self.message_label = tk.Label(root, text="Enter Your Message:", font=("Helvetica", 12), bg="lightblue")
        self.message_label.pack(pady=10)
        
        # Use Text widget for larger message input
        self.message_text = tk.Text(root, height=6, width=40, font=("Helvetica", 12))
        self.message_text.pack(pady=5)
        
        # Schedule Time (Date and Time)
        self.time_label = tk.Label(root, text="Schedule Time (e.g., HH:MM AM/PM MM/DD/YYYY):", font=("Helvetica", 12), bg="lightblue")
        self.time_label.pack(pady=10)
        self.time_entry = tk.Entry(root, width=20, font=("Helvetica", 12))
        self.time_entry.pack(pady=5)

        # Schedule Button
        self.schedule_button = tk.Button(root, text="Schedule Message", font=("Helvetica", 12), bg="lightgreen", command=self.schedule_message)
        self.schedule_button.pack(pady=20)

    def schedule_message(self):
        # Get the user's phone number, recipient, message, and schedule time
        user_phone_number = self.phone_number_entry.get()
        recipient = self.recipient_entry.get()
        message = self.message_text.get("1.0", tk.END).strip()  # Get the message from the Text widget
        schedule_time = self.time_entry.get()

        # Ensure that all required fields are filled
        if not user_phone_number or not recipient or not message or not schedule_time:
            messagebox.showwarning("Input Error", "Please enter all fields.")
            return
        
        # Prepare the signal-cli command to send the message
        signal_command = f'signal-cli -u {user_phone_number} send -m "{message}" {recipient}'
        
        # Create the full command to be scheduled using 'at'
        full_command = f"echo '{signal_command}' | at {schedule_time}"
        
        try:
            # Execute the command to schedule the message using 'at'
            subprocess.run(full_command, shell=True, check=True)
            messagebox.showinfo("Scheduled", f"Message scheduled for {schedule_time}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to schedule message: {str(e)}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SignalSchedulerGUI(root)
    root.mainloop()
