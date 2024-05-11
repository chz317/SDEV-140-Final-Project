import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class CapacityCounterApp:
    def __init__(self, master):
        # Initialize the application
        self.master = master
        self.max_capacity = 100  # Default max capacity
        self.current_count = 0

        # Load images
        self.increment_img = Image.open("enter.webp")  # Load the increment image
        self.decrement_img = Image.open("exit.jpg")     # Load the decrement image

        # Resize images if needed
        self.increment_img = self.increment_img.resize((32, 32))  # Resize the increment image
        self.decrement_img = self.decrement_img.resize((32, 32))  # Resize the decrement image

        # Convert images to tkinter format
        self.increment_photo = ImageTk.PhotoImage(self.increment_img)  # Convert increment image to PhotoImage
        self.decrement_photo = ImageTk.PhotoImage(self.decrement_img)  # Convert decrement image to PhotoImage

        # Create and display GUI elements
        self.display_label = tk.Label(master, text="Current Count: 0")  # Create label to display count
        self.display_label.pack()

        self.increment_button = tk.Button(master, image=self.increment_photo, command=self.increment)  # Create increment button
        self.increment_button.pack()

        self.decrement_button = tk.Button(master, image=self.decrement_photo, command=self.decrement)  # Create decrement button
        self.decrement_button.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)       # Create reset button
        self.reset_button.pack()

        self.settings_button = tk.Button(master, text="Settings", command=self.open_settings)  # Create settings button
        self.settings_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=self.exit)           # Create exit button
        self.exit_button.pack()

    def increment(self):
        # Increment the count if not at maximum capacity
        if self.current_count < self.max_capacity:
            self.current_count += 1
            self.update_display()  # Update display with new count
        else:
            messagebox.showinfo("Error", "Maximum capacity reached!")  # Show error message if at maximum capacity

    def decrement(self):
        # Decrement the count if greater than 0
        if self.current_count > 0:
            self.current_count -= 1
            self.update_display()  # Update display with new count

    def reset(self):
        # Reset the count to 0
        self.current_count = 0
        self.update_display()  # Update display with new count

    def open_settings(self):
        # Open settings window
        settings_window = tk.Toplevel(self.master)
        settings_window.title("Settings")

        # Create entry for new max capacity
        self.max_capacity_entry = tk.Entry(settings_window)
        self.max_capacity_entry.pack()

        # Create apply button to apply new settings
        apply_button = tk.Button(settings_window, text="Apply", command=self.apply_settings)
        apply_button.pack()

    def apply_settings(self):
        try:
            # Get new max capacity from entry and convert to integer
            new_capacity = int(self.max_capacity_entry.get())
            if new_capacity > 0:
                # Update max capacity and display new count
                self.max_capacity = new_capacity
                messagebox.showinfo("Success", "Settings applied successfully!")  # Show success message
                self.update_display()  # Update display with new count
            else:
                messagebox.showerror("Error", "Capacity should be a positive number!")  # Show error message for negative capacity
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Please enter a valid number.")  # Show error message for non-integer input

    def update_display(self):
        # Update display label with current count
        self.display_label.config(text=f"Current Count: {self.current_count}")

    def exit(self):
        # Ask user for confirmation before closing the application
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.master.destroy()  # Destroy the tkinter window

def main():
    # Create tkinter window and start the application
    root = tk.Tk()
    root.title("Capacity Counter")
    app = CapacityCounterApp(root)
    root.mainloop()  # Start the tkinter event loop

if __name__ == "__main__":
    main()  # Run the main function
