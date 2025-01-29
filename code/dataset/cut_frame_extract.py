import tkinter as tk
from tkinter import filedialog

def select_file():
    # Open a file dialog and get the selected file's path
    file_path = filedialog.askopenfilename(title="Select a file")
    
    # If a file is selected, display the file path
    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file selected")

def main():
    # Create the main window (it won't be shown, we just need it for the dialog)
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Call the function to open the file dialog
    select_file()

if __name__ == "__main__":
    main()
