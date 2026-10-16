import sqlite3
import tkinter
import tkinter.messagebox
import tkinter.ttk

def lection18():
    """
    tkinter + sqlite3
    """
    class ContactManager:
        def __init__(self, root):
            self.root = root
            self.root.title("Contact Manager")
            self.root.geometry("700x500")
            
            # Initialize database
            self.init_database()
            
            # Setup UI
            self.setup_ui()
            
            # Load contacts
            self.load_contacts()
        
        def init_database(self):
            """Create SQLite database and table if not exists"""
            self.conn = sqlite3.connect('contacts.db')
            self.cursor = self.conn.cursor()
            
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT,
                    email TEXT,
                    address TEXT
                )
            ''')
            self.conn.commit()
        
        def setup_ui(self):
            """Setup the user interface"""
            # Input Frame
            input_frame = tkinter.ttk.LabelFrame(self.root, text="Contact Information", padding=10)
            input_frame.pack(fill="x", padx=10, pady=5)
            
            # Name
            tkinter.ttk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
            self.name_var = tkinter.StringVar()
            self.name_entry =  tkinter.ttk.Entry(input_frame, textvariable=self.name_var, width=30)
            self.name_entry.grid(row=0, column=1, pady=5, padx=5)
            
            # Phone
            tkinter.ttk.Label(input_frame, text="Phone:").grid(row=0, column=2, sticky="w", pady=5, padx=(20,0))
            self.phone_var = tkinter.StringVar()
            self.phone_entry = tkinter.ttk.Entry(input_frame, textvariable=self.phone_var, width=30)
            self.phone_entry.grid(row=0, column=3, pady=5, padx=5)
            
            # Email
            tkinter.ttk.Label(input_frame, text="Email:").grid(row=1, column=0, sticky="w", pady=5)
            self.email_var = tkinter.StringVar()
            self.email_entry = tkinter.ttk.Entry(input_frame, textvariable=self.email_var, width=30)
            self.email_entry.grid(row=1, column=1, pady=5, padx=5)
            
            # Address
            tkinter.ttk.Label(input_frame, text="Address:").grid(row=1, column=2, sticky="w", pady=5, padx=(20,0))
            self.address_var = tkinter.StringVar()
            self.address_entry = tkinter.ttk.Entry(input_frame, textvariable=self.address_var, width=30)
            self.address_entry.grid(row=1, column=3, pady=5, padx=5)
            
            # Buttons Frame
            button_frame = tkinter.ttk.Frame(self.root)
            button_frame.pack(fill="x", padx=10, pady=5)
            
            tkinter.ttk.Button(button_frame, text="Add Contact", command=self.add_contact).pack(side="left", padx=5)
            tkinter.ttk.Button(button_frame, text="Update Contact", command=self.update_contact).pack(side="left", padx=5)
            tkinter.ttk.Button(button_frame, text="Delete Contact", command=self.delete_contact).pack(side="left", padx=5)
            tkinter.ttk.Button(button_frame, text="Clear Fields", command=self.clear_fields).pack(side="left", padx=5)
            
            # Search Frame
            search_frame = tkinter.ttk.Frame(self.root)
            search_frame.pack(fill="x", padx=10, pady=5)
            
            tkinter.ttk.Label(search_frame, text="Search:").pack(side="left", padx=5)
            self.search_var = tkinter.StringVar()
            self.search_entry = tkinter.ttk.Entry(search_frame, textvariable=self.search_var, width=30)
            self.search_entry.pack(side="left", padx=5)
            tkinter.ttk.Button(search_frame, text="Search", command=self.search_contacts).pack(side="left", padx=5)
            tkinter.ttk.Button(search_frame, text="Show All", command=self.load_contacts).pack(side="left", padx=5)
            
            # Treeview (Table)
            columns = ("ID", "Name", "Phone", "Email", "Address")
            self.tree = tkinter.ttk.Treeview(self.root, columns=columns, show="headings", height=15)
            
            # Define headings
            for col in columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=120)
            
            self.tree.column("ID", width=50)
            self.tree.pack(fill="both", expand=True, padx=10, pady=5)
            
            # Scrollbar
            scrollbar = tkinter.ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
            scrollbar.pack(side="right", fill="y")
            self.tree.configure(yscrollcommand=scrollbar.set)
            
            # Bind selection event
            self.tree.bind("<<TreeviewSelect>>", self.on_select)
        
        def add_contact(self):
            """Add a new contact to the database"""
            name = self.name_var.get().strip()
            phone = self.phone_var.get().strip()
            email = self.email_var.get().strip()
            address = self.address_var.get().strip()
            
            if not name:
                tkinter.messagebox.showwarning("Warning", "Name is required!")
                return
            
            try:
                self.cursor.execute('''
                    INSERT INTO contacts (name, phone, email, address)
                    VALUES (?, ?, ?, ?)
                ''', (name, phone, email, address))
                self.conn.commit()
                
                tkinter.messagebox.showinfo("Success", "Contact added successfully!")
                self.clear_fields()
                self.load_contacts()
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"Failed to add contact: {e}")
        
        def load_contacts(self):
            """Load all contacts into the treeview"""
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            try:
                self.cursor.execute("SELECT * FROM contacts ORDER BY name")
                contacts = self.cursor.fetchall()
                
                for contact in contacts:
                    self.tree.insert("", "end", values=contact)
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"Failed to load contacts: {e}")
        
        def search_contacts(self):
            """Search contacts by name or phone"""
            search_term = self.search_var.get().strip()
            
            if not search_term:
                self.load_contacts()
                return
            
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            try:
                self.cursor.execute('''
                    SELECT * FROM contacts 
                    WHERE name LIKE ? OR phone LIKE ?
                    ORDER BY name
                ''', (f'%{search_term}%', f'%{search_term}%'))
                
                contacts = self.cursor.fetchall()
                
                if contacts:
                    for contact in contacts:
                        self.tree.insert("", "end", values=contact)
                else:
                    tkinter.messagebox.showinfo("Info", "No contacts found!")
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"Search failed: {e}")
        
        def on_select(self, event):
            """Handle selection from treeview"""
            selected_item = self.tree.selection()
            if selected_item:
                values = self.tree.item(selected_item[0], "values")
                if values:
                    self.name_var.set(values[1])
                    self.phone_var.set(values[2])
                    self.email_var.set(values[3])
                    self.address_var.set(values[4])
        
        def update_contact(self):
            """Update selected contact"""
            selected_item = self.tree.selection()
            if not selected_item:
                tkinter.messagebox.showwarning("Warning", "Please select a contact to update!")
                return
            
            contact_id = self.tree.item(selected_item[0], "values")[0]
            name = self.name_var.get().strip()
            phone = self.phone_var.get().strip()
            email = self.email_var.get().strip()
            address = self.address_var.get().strip()
            
            if not name:
                tkinter.messagebox.showwarning("Warning", "Name is required!")
                return
            
            try:
                self.cursor.execute('''
                    UPDATE contacts 
                    SET name=?, phone=?, email=?, address=?
                    WHERE id=?
                ''', (name, phone, email, address, contact_id))
                self.conn.commit()
                
                tkinter.messagebox.showinfo("Success", "Contact updated successfully!")
                self.clear_fields()
                self.load_contacts()
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"Failed to update contact: {e}")
        
        def delete_contact(self):
            """Delete selected contact"""
            selected_item = self.tree.selection()
            if not selected_item:
                tkinter.messagebox.showwarning("Warning", "Please select a contact to delete!")
                return
            
            contact_id = self.tree.item(selected_item[0], "values")[0]
            contact_name = self.tree.item(selected_item[0], "values")[1]
            
            if tkinter.messagebox.askyesno("Confirm", f"Are you sure you want to delete '{contact_name}'?"):
                try:
                    self.cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
                    self.conn.commit()
                    
                    tkinter.messagebox.showinfo("Success", "Contact deleted successfully!")
                    self.clear_fields()
                    self.load_contacts()
                except Exception as e:
                    tkinter.messagebox.showerror("Error", f"Failed to delete contact: {e}")
        
        def clear_fields(self):
            """Clear all input fields"""
            self.name_var.set("")
            self.phone_var.set("")
            self.email_var.set("")
            self.address_var.set("")
            self.search_var.set("")
            self.name_entry.focus()
        
        def __del__(self):
            """Close database connection when closing the app"""
            if hasattr(self, 'conn'):
                self.conn.close()

    root = tkinter.Tk()
    app = ContactManager(root)
    root.mainloop()

