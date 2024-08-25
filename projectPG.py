import tkinter as tk
from tkinter import messagebox, Scrollbar, Text
import string
import random

# Function to generate the password
def generate_password():
    try:
        # Get the number of characters from the user input
        characters_number = int(entry.get())

        # Validate the number of characters
        if characters_number < 6:
            messagebox.showerror("Error", "You need at least 6 characters.")
            return
        if characters_number > 15:
            messagebox.showerror("Error", "The maximum number of characters is 15.")
            return

        # Define the character sets
        s1 = list(string.ascii_lowercase)  # Lowercase letters
        s2 = list(string.ascii_uppercase)  # Uppercase letters
        s3 = list(string.digits)  # Digits
        s4 = list(string.punctuation)  # Special characters

        # Calculate parts of the password
        part1 = round(characters_number * 0.30)
        part2 = round(characters_number * 0.20)

        # Calculate the remaining characters
        remaining_characters = characters_number - (part1 * 2 + part2 * 2)

        # Generate the password
        password = []
        password += random.sample(s1, part1)
        password += random.sample(s2, part1)
        password += random.sample(s3, part2)
        password += random.sample(s4, part2)
        password += random.choices(s1 + s2 + s3 + s4, k=remaining_characters)

        # Shuffle the password and convert to string
        random.shuffle(password)
        password_str = ''.join(password)

        # Display the generated password
        result_var.set(password_str)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x500")
root.configure(bg="#F8F9FA")  # Light background color

# Create and place widgets with simplified design
header_frame = tk.Frame(root, bg="#E9ECEF", pady=10)
header_frame.pack(fill='x')

tk.Label(header_frame, text="Password Generator", font=("Arial", 20, "bold"), bg="#E9ECEF").pack()

main_frame = tk.Frame(root, bg="#F8F9FA", pady=20)
main_frame.pack(pady=20)

tk.Label(main_frame, text="Enter the number of characters:", font=("Arial", 12), bg="#F8F9FA").pack(pady=5)

entry = tk.Entry(main_frame, font=("Arial", 14), width=15, justify='center')
entry.pack(pady=5)

generate_button = tk.Button(main_frame, text="Generate Password", font=("Arial", 14), bg="#007BFF", fg="#FFFFFF", relief='flat', command=generate_password)
generate_button.pack(pady=20, fill='x')

result_var = tk.StringVar()
result_label = tk.Label(main_frame, textvariable=result_var, font=("Arial", 14), bg="#F8F9FA")
result_label.pack(pady=10)

# Terms and Conditions
terms_frame = tk.Frame(root, bg="#F8F9FA")
terms_frame.pack(fill='both', pady=10, padx=20)

terms_label = tk.Label(terms_frame, text="Terms and Conditions:", font=("Arial", 14, "bold"), bg="#F8F9FA")
terms_label.pack(anchor='w')

terms_text = """Terms and Conditions

1. **Minimum Length**: The password must be at least 6 characters long.
2. **Maximum Length**: The password can be up to 15 characters long.
3. **Character Sets**: Passwords will include a mix of lowercase letters, uppercase letters, digits, and special characters.
4. **Security**: Ensure your password is kept secure and not shared with others.
5. **Usage**: This tool is for generating secure passwords and should be used responsibly.

By using this tool, you agree to these terms and conditions."""

# Create a text widget with scrollbars
terms_text_widget = tk.Text(terms_frame, wrap='word', height=10, width=50, font=("Arial", 12), bg="#E9ECEF", fg="#212529", padx=10, pady=10)
terms_text_widget.insert(tk.END, terms_text)
terms_text_widget.config(state=tk.DISABLED)  # Make the text widget read-only

scroll_y = Scrollbar(terms_frame, orient=tk.VERTICAL, command=terms_text_widget.yview)
terms_text_widget.config(yscrollcommand=scroll_y.set)

terms_text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

# Start the GUI event loop
root.mainloop()
