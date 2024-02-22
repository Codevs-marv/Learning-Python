import helpers
import database as db
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING


class CenterWidgetMixin:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        self.geometry(f'{w}x{h}+{x}+{y}')

class CreateClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Crear cliente')
        self.build()
        self.center()
        self.transient(parent)
        self.grab_set()

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text='CC (2 ints y 1 upper char)').grid(row=0, column=0)
        Label(frame, text='Nombre (de 2 a 30 chars)').grid(row=0, column=1)
        Label(frame, text='Apellido (de 2 a 30 chars)').grid(row=0, column=2)

        cc = Entry(frame)
        cc.grid(row=1, column=0)
        cc.bind('<keyRelease>', lambda event: self.validate(event, 0))
        nombre = Entry(frame)
        nombre.grid(row=1, column=1)
        nombre.bind('<keyRelease>', lambda event: self.validate(event, 1))
        apellido = Entry(frame)
        apellido.grid(row=1, column=2)
        apellido.bind('<keyRelease>', lambda event: self.validate(event, 2))

        frame = Frame(self)
        frame.pack(pady=10)

        crear = Button(frame, text='Crear', command=self.create_client)
        crear.configure(state=DISABLED)
        crear.grid(row=0, column=0)
        Button(frame, text='Cancelar', command=self.close).grid(row=0, column=1)


    def create_client(self):
        pass
    
    def close(self):
        self.destroy()
        self.update()
    
    def validate(self, event, index):
        valor = event.widget.get()
        valido = helpers.cc_valido(valor, db.Clientes.lista) if index == 0 \
            else (valor.isalpha() and len(valor) >= 2 and len(valor) <= 30)
        event.widget.configure({"bg": "Green" if valido else "Red"})
            


class MainWindow(Tk, CenterWidgetMixin):
    def __init__(self):
        super().__init__()
        self.title('Gestor de Clientes')
        self.build()
        self.center()

    def build(self):
        frame = Frame(self)
        frame.pack()

        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('CC', 'Nombre', 'Apellido')

        treeview.column('#0', width=0, stretch=NO)
        treeview.column('CC', anchor=CENTER)
        treeview.column('Nombre', anchor=CENTER)
        treeview.column('Apellido', anchor=CENTER)

        treeview.heading('CC', text='CC', anchor=CENTER)
        treeview.heading('Nombre', text='Nombre', anchor=CENTER)
        treeview.heading('Apellido', text='Apellido', anchor=CENTER)

        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        treeview['yscrollcommand'] = scrollbar.set

        for cliente in db.Clientes.lista:
            treeview.insert(
                parent='', index='end', iid=cliente.cc,
                values=(cliente.cc, cliente.nombre, cliente.apellido))


        treeview.pack()

        frame = Frame(self)
        frame.pack(pady=20)

        Button(frame, text='Crear', command=self.create).grid(row=0, column=0)
        Button(frame, text='Editar', command=None).grid(row=0, column=1)
        Button(frame, text='Borrar', command=self.delete).grid(row=0, column=2)

        self.treeview = treeview


    def delete(self):
        cliente = self.treeview.focus()
        if cliente:
            campos = self.treeview.item(cliente, 'values')
            confirmar = askokcancel(
                title='Confirmar borrado',
                message=f'¿Borrar a {campos[1]} {campos[2]}?',
                icon=WARNING)
            if confirmar:
                self.treeview.delete(cliente)


    def create(self):
        CreateClientWindow(self)  





if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
