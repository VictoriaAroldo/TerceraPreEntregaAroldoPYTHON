class cliente:
    
    def __init__(self, nombre, mail, tel, direccion):
        self.nombre = input("Nombre(s): ")
        self.apellido = apellido
        self.mail = mail
        self.tel = tel
        self.direccion = direccion
    
    def __str__(self):
        return f"NOMBRE {self.nombre}"


    def hacer_compra(self, producto):
        print(f"{self.nombre} compró {producto}.")  

