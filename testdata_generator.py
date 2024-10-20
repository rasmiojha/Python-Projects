import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
from datetime import datetime, timedelta
import pandas as pd

class TestDataGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Test Data Generator")
        self.root.geometry("400x400")

        self.data_type_label = ttk.Label(root, text="Select Data Type:")
        self.data_type_label.pack(pady=5)

        self.data_type = ttk.Combobox(root, values=["Numeric", "Varchar", "Date", "String", "Float", "Boolean"])
        self.data_type.pack(pady=5)
        self.data_type.current(0)

        self.count_label = ttk.Label(root, text="Number of samples:")
        self.count_label.pack(pady=5)

        self.count_entry = ttk.Entry(root)
        self.count_entry.pack(pady=5)

        self.file_format_label = ttk.Label(root, text="Select File Format:")
        self.file_format_label.pack(pady=5)

        self.file_format = ttk.Combobox(root, values=["Excel", "CSV", "Parquet"])
        self.file_format.pack(pady=5)
        self.file_format.current(0)

        self.filename_label = ttk.Label(root, text="Enter Filename:")
        self.filename_label.pack(pady=5)

        self.filename_entry = ttk.Entry(root)
        self.filename_entry.pack(pady=5)

        self.generate_button = ttk.Button(root, text="Generate", command=self.generate_data)
        self.generate_button.pack(pady=20)

        self.result_text = tk.Text(root, height=10, width=40)
        self.result_text.pack(pady=5)

    def generate_data(self):
        data_type = self.data_type.get()
        file_format = self.file_format.get()
        filename = self.filename_entry.get().strip()

        try:
            count = int(self.count_entry.get())
            if count <= 0:
                raise ValueError("Number of samples must be greater than 0.")
        except ValueError as e:
            messagebox.showerror("Invalid input", str(e))
            return

        if not filename:
            messagebox.showerror("Invalid input", "Filename cannot be empty.")
            return

        data = []
        if data_type == "Numeric":
            data = [random.randint(0, 100) for _ in range(count)]
        elif data_type == "Varchar":
            data = [''.join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in range(count)]
        elif data_type == "Date":
            start_date = datetime(2000, 1, 1)
            end_date = datetime(2025, 12, 31)
            data = [(start_date + timedelta(days=random.randint(0, (end_date - start_date).days))).strftime('%Y-%m-%d') for _ in range(count)]
        elif data_type == "String":
            data = [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(count)]
        elif data_type == "Float":
            data = [round(random.uniform(0.0, 100.0), 2) for _ in range(count)]
        elif data_type == "Boolean":
            data = [random.choice([True, False]) for _ in range(count)]

        df = pd.DataFrame(data, columns=[data_type])

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "\n".join(map(str, data)))

        filename_with_ext = f"{filename}.{file_format.lower()}"

        try:
            if file_format == "Excel":
                df.to_excel(filename_with_ext, index=False, engine='openpyxl')
            elif file_format == "CSV":
                df.to_csv(filename_with_ext, index=False, sep='/')
            elif file_format == "Parquet":
                df.to_parquet(filename_with_ext, index=False)
            else:
                messagebox.showerror("Invalid format", "Unsupported file format selected.")
                return
            messagebox.showinfo("Success", f"Data saved as {filename_with_ext}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = TestDataGenerator(root)
    root.mainloop()
