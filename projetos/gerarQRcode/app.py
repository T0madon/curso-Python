import tkinter as tk
from tkinter import messagebox
import db
import qr_generator
import sqlite3

db.initialize_db()

db.add_product("Produto A", 10)
db.add_product("Produto B", 5)
db.add_product("Produto C", 20)

class SalesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Vendas")
        self.create_widgets()
    
    def create_widgets(self):
        
        self.product_listbox = tk.Listbox(self.root)
        self.product_listbox.pack()
        
        self.generate_button = tk.Button(self.root, text="Gerar Ticket", command=self.generate_ticket)
        self.generate_button.pack()

        self.update_product_list()
    
    def update_product_list(self):
        self.product_listbox.delete(0, tk.END)
        products = db.get_products()
        for product in products:
            self.product_listbox.insert(tk.END, f"{product[1]} - Quantidade: {product[2]}")

    def generate_ticket(self):
        selected_index = self.product_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Seleção Inválida", "Selecione um produto para gerar o ticket.")
            return

        product = db.get_products()[selected_index[0]]
        product_id, name, quantity = product
        
        # Inserir o ticket no banco
        conn = sqlite3.connect("sales_app.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tickets (product_id) VALUES (?)", (product_id,))
        ticket_id = cursor.lastrowid
        conn.commit()
        conn.close()

        # Gerar QR code
        qr_data = f"ticket_id:{ticket_id}"
        qr_filename = qr_generator.generate_qr_code(qr_data)

        # Exibir mensagem de sucesso
        messagebox.showinfo("QR Code Gerado", f"QR Code gerado para {name}. Salvo em {qr_filename}")
        self.update_product_list()

# Iniciar o aplicativo
if __name__ == "__main__":
    root = tk.Tk()
    app = SalesApp(root)
    root.mainloop()

