from paquete import cliente

clientes = {}

def registrar_usuario():
    print("Registro de nuevo usuario:")
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    contrasenia = input("Ingrese la contraseña: ")

    if nombre_usuario in clientes:
        print("El nombre de usuario ya existe. Por favor, elija otro nombre de usuario.\n")
        registrar_usuario()
    else:
        print("Para completar el registro, ingrese sus datos personales:")
        print("-----------------------------------------------------------")
    
        nombre = input("Nombre(s): ")
        apellido = input("Apellio(s): ")
        mail = input("Correo electrónico: ")
        tel = int(input("Teléfono de contacto: "))
        direccion = input("Dirección de facturación (para futuras compras): ")

        """def numtel(tel):
            if tel.strip().isdigit():
                direccion = input("Dirección de facturación (para futuras compras): ")   
            else:
                print("El dato que ingresaste no es un número de teléfono. Por favor, ingrese solo números.")
                tel = int(input("Teléfono de contacto: "))"""
        
        
        clientes[nombre_usuario] = contrasenia
        print("Usuario registrado con éxito.\n")


def mostrar_clientes():
    if clientes:
        print("Usuarios ya registrados en nuestra base de datos:")
        print("-------------------------------------------------")
        for nombre_usuario, contrasena in clientes.items():
          print(f"{nombre_usuario}")
          print("-------------------------------------------------")

    else:
        print("No hay usuarios registrados en la base de datos.\n")


def login():
    print("Iniciar sesión:")
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    contrasenia = input("Ingrese su contraseña: ")
    
    def menu2():
                while nombre_usuario in clientes and clientes[nombre_usuario] == contrasenia:
                    print(f"Bienvenidx, {nombre_usuario} a nuestra tienda virtual!\n")
                
                    print("1. Realizar una compra")
                    print("2. Ver datos personales")
                    print("3. Salir")

                    def menu3():
                        if (opcion3 == 1):
                            print("--------------------------------")
                            print("LISTADO DE PRODUCTOS DISPONIBLES")
                            print("--------------------------------")
                            print("1. Laptop")
                            print("2. Botella de agua")
                            print("3. Mate")

                            def menu4():
                                if (info == 1):
                                    print("Una cómoda computadora. $100")

                                    print("1. Comprar")
                                    print("2. Volver al menú de productos")

                                    comprar = int(input("Desea hacer esta compra?: "))

                                    if(comprar == 1):
                                        print ("Gracias por su compra")
                                    elif(comprar == 2):
                                        menu3() 
                                    else:
                                        print("Ingrese una opción válida.")
                                        menu4()

                                elif(info == 2):
                                    print("Una botella muy práctica para llevar agua. $25")

                                    print("1. Comprar")
                                    print("2. Volver al menú de productos")

                                    comprar = int(input("Desea hacer esta compra?: "))

                                    if(comprar == 1):
                                        print ("Gracias por su compra")
                                    elif(comprar == 2):
                                        menu3() 
                                    else:
                                        print("Ingrese una opción válida.")
                                        menu4()
                                        
                                elif(info == 3):
                                    print("Un mate muy rico y amargo. $10")

                                    print("1. Comprar")
                                    print("2. Volver al menú de productos")

                                    comprar = int(input("Desea hacer esta compra?: "))

                                    if(comprar == 1):
                                        print ("Gracias por su compra")
                                    elif(comprar == 2):
                                        menu3() 
                                    else:
                                        print("Ingrese una opción válida.")
                                        menu4()
                                else:
                                    print("Por favor, ingrese una opción válida.")
                                    menu3()

                            info = int(input("Para más infomación, ingrese el código numérico del producto: ")) 
                            menu4()
                        
                        elif(opcion3 == 2):
                            
                            def mostrar_datos():
                                datos = input("Ingrese su contraseña para mostrar sus datos: ")
                                if((nombre_usuario in clientes and clientes[nombre_usuario] == contrasenia) and datos == contrasenia):
                                    print(f"Nombre: {main.registrar_usuario.nombre}\n")
                                    print(f"Apellido: {main.registrar_usuario.apellido}\n")
                                    print(f"Correo electrónico: {main.registrar_usuario.mail}\n")
                                    print(f"Teléfono de contacto: {main.registrar_usuario.tel}\n")
                                    print(f"Dirección de facturación: {main.registrar_usuario.direccion}\n")
                                else:
                                    print("Contraseña incorrecta.")
                                    def menu6():
                                        opcion4 = int(input("Qué desea hacer? :"))
                                        print("1. Intentar de nuevo.\n")
                                        print("2. Salir\n")

                                        if(opcion4 == 1):
                                            mostrar_datos()
                                        elif(opcion4 == 2):
                                            menu2()
                                        else:
                                            print("Opción inválida. Por favor, ingrese una opción válida.\n")
                                            menu6()
                                    menu6()
                            mostrar_datos()
                        
                        elif(opcion3 == 3):
                            print("Nos vemos!")
                            #break 
                        
                        else:
                            print("Opción inválida. Por favor, ingrese una opción válida.\n")
                            menu2()
                               
                    opcion3 = int(input("Qué desea hacer?: "))
                    menu3()

                    
    if nombre_usuario in clientes:

        if clientes[nombre_usuario] == contrasenia:
            menu2()    
            
        else:
            print("Nombre de usuario o contraseña incorrectos. Por favor, inténtelo de nuevo.\n")
            login()

    else:
         def menu5():
            print("El usuario no está registrado en la base de datos. Registre su usuario o intentelo de nuevo")
            print("1.Registrar usuario")
            print("2.Intentar de nuevo")
            print("3.Salir")

            opcion = input("¿Qué desea hacer?: ")

            if (opcion == "1"):
                registrar_usuario()
            elif (opcion == "2"):
                login()
            elif (opcion == "3"):
                print("Nos vemos!")
            else:
                print("Opción inválida. Por favor, ingrese una opción válida.\n")
                menu5()
         menu5()
    

            

            

    #if nombre_usuario in clientes and clientes[nombre_usuario] == contrasenia:
        #print(f"Bienvenidx, {nombre_usuario}!\n")

def menu1():
    while True:
        print("Bienvenidx al registro de usuarios!")
        print("1. Registrar nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Iniciar sesión")
        print("4. Salir")
        opcion2 = input("Ingrese el número de la opción que desee: ")

        if opcion2 == "1":
            registrar_usuario()
        elif opcion2 == "2":
            mostrar_clientes()
        elif opcion2 == "3":
            login()
        elif opcion2 == "4":
            print("Nos vemos!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.\n")

if __name__ == "__main__":
    menu1()
else:
    print ("El programa no pudo ejecutarse o fue cerrado por el usuario.")

#cliente0 = cliente("María", "Fernández", "MFernandez@gmail.com", "Av. Córdoba 1234", "CABA")
#cliente1 = cliente("Luis Alberto", "Spinetta", "luisalber@gmail.com", "Iberá 5009", "CABA")

#print ("Nuestros clientes de hoy:")
#print("-----------------------------")
#print(cliente1)
#print(cliente2)

#cliente0.actualizar_datos(apellido="Lopez")

#cliente1.hacer_compra("Parlantes SEISA")

#cliente2.cambiar_datos(nombre="María Gómez")
#print ("Sus nuevos datos son:")
#print(cliente2.nombre)

#confirmar = input ("Desea confirmar sus nuevos datos?:")
#print("1. Sí")
#print("2. No")
#if (confirmar == "1"):


