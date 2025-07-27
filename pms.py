import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pandas as pd

products = []
sales = []
customers = []

class StockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Management System")
        self.root.geometry("800x600")
        self.root.configure(bg="#333333")  # Dark gray background

        self.create_ribbon_menu()

        # Main content area
        self.content_frame = tk.Frame(self.root, bg="#333333")
        self.content_frame.pack(expand=True, fill=tk.BOTH)

    def create_ribbon_menu(self):
        """Creates the main ribbon menu with Product, Customer, and Sales buttons."""
        ribbon_frame = tk.Frame(self.root, bg="#444444")
        ribbon_frame.pack(side=tk.TOP, fill=tk.X)

        # Product Button
        product_button = tk.Button(ribbon_frame, text="Product", command=self.show_product_menu, bg="#007bff", fg="white", font=("Helvetica", 12), width=10)
        product_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Customer Button
        customer_button = tk.Button(ribbon_frame, text="Customer", command=self.show_customer_menu, bg="#007bff", fg="white", font=("Helvetica", 12), width=10)
        customer_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Sales Button
        sales_button = tk.Button(ribbon_frame, text="Sales", command=self.show_sales_menu, bg="#007bff", fg="white", font=("Helvetica", 12), width=10)
        sales_button.pack(side=tk.LEFT, padx=10, pady=10)

    def show_product_menu(self):
        self.clear_content_frame()
        title = tk.Label(self.content_frame, text="Product Management", font=("Helvetica", 18, "bold"), bg="#333333", fg="#007bff")
        title.pack(pady=20)

        add_product_button = tk.Button(self.content_frame, text="Add Product", command=self.show_add_product, bg="#007bff", fg="white", font=("Helvetica", 12))
        add_product_button.pack(pady=10)

        view_product_button = tk.Button(self.content_frame, text="View Products", command=self.show_view_products, bg="#007bff", fg="white", font=("Helvetica", 12))
        view_product_button.pack(pady=10)

    def show_customer_menu(self):
        self.clear_content_frame()
        title = tk.Label(self.content_frame, text="Customer Management", font=("Helvetica", 18, "bold"), bg="#333333", fg="#007bff")
        title.pack(pady=20)

        add_customer_button = tk.Button(self.content_frame, text="Add Customer", command=self.show_add_customer, bg="#007bff", fg="white", font=("Helvetica", 12))
        add_customer_button.pack(pady=10)

        view_customer_button = tk.Button(self.content_frame, text="View Customers", command=self.show_view_customers, bg="#007bff", fg="white", font=("Helvetica", 12))
        view_customer_button.pack(pady=10)

    def show_sales_menu(self):
        self.clear_content_frame()
        title = tk.Label(self.content_frame, text="Sales Management", font=("Helvetica", 18, "bold"), bg="#333333", fg="#007bff")
        title.pack(pady=20)

        add_sales_button = tk.Button(self.content_frame, text="Add Sales", command=self.show_add_sales, bg="#007bff", fg="white", font=("Helvetica", 12))
        add_sales_button.pack(pady=10)

        view_sales_button = tk.Button(self.content_frame, text="View Sales", command=self.show_view_sales, bg="#007bff", fg="white", font=("Helvetica", 12))
        view_sales_button.pack(pady=10)

    def show_add_product(self):
        self.clear_content_frame()

        title = tk.Label(self.content_frame, text="Add Product", font=("Helvetica", 18, "bold"), bg="#333333", fg="#007bff")
        title.pack(pady=20)

        product_name_label = tk.Label(self.content_frame, text="Product Name", bg="#333333", fg="white", font=("Helvetica", 12))
        product_name_label.pack(pady=5)
        product_name_entry = tk.Entry(self.content_frame)
        product_name_entry.pack(pady=5)

        quantity_label = tk.Label(self.content_frame, text="Quantity", bg="#333333", fg="white", font=("Helvetica", 12))
        quantity_label.pack(pady=5)
        quantity_entry = tk.Entry(self.content_frame)
        quantity_entry.pack(pady=5)

        price_label = tk.Label(self.content_frame, text="Price", bg="#333333", fg="white", font=("Helvetica", 12))
        price_label.pack(pady=5)
        price_entry = tk.Entry(self.content_frame)
        price_entry.pack(pady=5)

        def add_product():
            product = {
                'name': product_name_entry.get(),
                'quantity': quantity_entry.get(),
                'price': price_entry.get()
            }
            products.append(product)
            messagebox.showinfo("Success", "Product is added")

        add_product_button = tk.Button(self.content_frame, text="Add Product", command=add_product, bg="#007bff", fg="white", font=("Helvetica", 12))
        add_product_button.pack(pady=10)

    def show_view_products(self):
        self.clear_content_frame()

        title = tk.Label(self.content_frame, text="View Products", font=("Helvetica", 18, "bold"), bg="#333333", fg="#007bff")
        title.pack(pady=20)

        columns = ('product_name', 'quantity', 'price')
        tree = ttk.Treeview(self.content_frame, columns=columns, show='headings', height=10)
        tree.heading('product_name', text='Product Name')
        tree.heading('quantity', text='Quantity')
        tree.heading('price', text='Price')

        for product in products:
            tree.insert('', tk.END, values=(product['name'], product['quantity'], product['price']))

        tree.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

        # Add Download button
        download_button = tk.Button(self.content_frame, text="Download Products", command=lambda: self.download_data('products'), bg="#007bff", fg="white", font=("Helvetica", 12))
        download_button.pack(pady=10)

    def show_add_sales(self):
        self.clear_content_frame()

        title = tk.Label(self.content_frame, text="Add Sales", font=("Helvetica", 18, "bold"), bg="#333333", fg="#007bff")
        title.pack(pady=20)

        product_name_label = tk.Label(self.content_frame, text="Product Name", bg="#333333", fg="white", font=("Helvetica", 12))
        product_name_label.pack(pady=5)
        product_name_entry = tk.Entry(self.content_frame)
        product_name_entry.pack(pady=5)

        quantity_label = tk.Label(self.content_frame, text="Quantity", bg="#333333", fg="white", font=("Helvetica", 12))
        quantity_label.pack(pady=5)
        quantity_entry = tk.Entry(self.content_frame)
        quantity_entry.pack(pady=5)

        price_label = tk.Label(self.content_frame, text="Price", bg="#333333", fg="white", font=("Helvetica", 12))
        price_label.pack(pady=5)
        price_entry = tk.Entry(self.content_frame)
        price_entry.pack(pady=5)

        customer_name_label = tk.Label(self.content_frame, text="Customer Name", bg="#333333", fg="white", font=("Helvetica", 12))
        customer_name_label.pack(pady=5)
        customer_name_entry = tk.Entry(self.content_frame)
        customer_name_entry.pack(pady=5)

        def add_sales():
            sale = {
                'product_name': product_name_entry.get(),
                'quantity': quantity_entry.get(),
                'price': price_entry.get(),
                'customer_name': customer_name_entry.get()
            }
            sales.append(sale)
            messagebox.showinfo("Success", "Sale is added")

        add_sales_button = tk.Button(self.content_frame, text="Add Sales", command=add_sales, bg="#007bff", fg="white", font=("Helvetica", 12))
        add_sales_button.pack(pady=10)

    def show_view_sales(self):
        self.clear_content_frame()

        title = tk.Label(self.content_frame, text="View Sales", font=("Helvetica", 18, "bold"), bg="#333333", fg="#007bff")
        title.pack(pady=20)

        columns = ('product_name', 'quantity', 'price', 'customer_name')
        tree = ttk.Treeview(self.content_frame, columns=columns, show='headings', height=10)
        tree.heading('product_name', text='Product Name')
        tree.heading('quantity', text='Quantity')
        tree.heading('price', text='Price')
        tree.heading('customer_name', text='Customer Name')

        for sale in sales:
            tree.insert('', tk.END, values=(sale['product_name'], sale['quantity'], sale['price'], sale['customer_name']))

        tree.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

        # Add Download button
        download_button = tk.Button(self.content_frame, text="Download Sales", command=lambda: self.download_data('sales'), bg="#007bff", fg="white", font=("Helvetica", 12))
        download_button.pack(pady=10)

    def download_data(self, data_type):
        """Downloads product or sales data as an Excel sheet."""
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if not file_path:
            return

        if data_type == 'products':
            data = pd.DataFrame(products)
        elif data_type == 'sales':
            data = pd.DataFrame(sales)

        try:
            data.to_excel(file_path, index=False)
            messagebox.showinfo("Success", f"{data_type.capitalize()} data successfully downloaded!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download {data_type} data. Error: {str(e)}")

    def clear_content_frame(self):
        """Clears the content frame."""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = StockApp(root)
    root.mainloop()