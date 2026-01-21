import random
import pyqrcode
import png

detalleCompras =[[],[],[],[],[],[]]

def menuopciones():
    print("¿Que accion desea realizar?")
    print('*  1)Registrar pedidos')
    print('*  2)Mostrar pedidos')
    print('*  3)Mostrar detalle de un pedido')
    print('*  4)Eliminar pedido')
    print('*  5)Salir del sistema')
    return int(input("Ingrese la opcion: "))


def ingresarpedido():
    print("Ingrese los datos del cliente")
    nombre=input("Nombre: ")
    apellido=input("Apellido: ")
    telefono=input("Telefono: ")
    direccion=input("Direccion: ")
    detalleCompras[0].append(nombre)
    detalleCompras[1].append(apellido)
    detalleCompras[2].append(telefono)
    detalleCompras[3].append(direccion)
    detalleCompras[4].append(random.randrange(1000, 9999))
    print("Seleccione el paquete ofimatico a contratar")
    print("1)opcion 1: PC + Monitor = $500")
    print("2)opcion 2: PC + Monitor 4K = $2000")
    print("3)opcion 3: Laptop UltraProIA = $1500")
    print("4)opcion 4: Worstation servidor = $3000")
    opcion = int(input("Ingrese la opcion: "))
    if opcion == 1:
        detalleCompras[5].append(500+(0.15*500))
    elif opcion == 2:
        detalleCompras[5].append(2000+(0.15*2000))
    elif opcion == 3:
        detalleCompras[5].append(1500+(0.15*1500))
    elif opcion == 4:
        detalleCompras[5].append(3000+(0.15*3000))
    print("Pedido registrado exitosamente")

def mostrarpedido(i):
    print("Nombre: ",detalleCompras[0][i])
    print("Apellido: ",detalleCompras[1][i])
    print("Telefono: ",detalleCompras[2][i])
    print("Direccion: ",detalleCompras[3][i])
    print("Codigo de pedido: ",detalleCompras[4][i])
    print("Total a pagar con IVA: ",detalleCompras[5][i])


def mostrarPedidos():
    if len(detalleCompras[0]) == 0:
        print("No hay pedidos registrados")
        return 
    else:
        print("Lista de pedidos")
        for c in range(len(detalleCompras[0])):
            mostrarpedido(c)


def mostrarDetallePedido() :
    if len(detalleCompras[0])==0:
        print("No hay pedidos registrados ")
        return
    else:
        codigo = int(input("Ingrese el codigo del pedido: "))
        if codigo in detalleCompras[4]:
            codigoIndex = detalleCompras[4].index(codigo)
            mostrarPedidos(codigoIndex)
        else:
            print("El codigo ingresado no existe")

def eliminarPedido():
    codigo = int(input("Ingrese el codigo del pedido: "))
    if codigo in detalleCompras[4]:
        codigoIndex = detalleCompras[4].index(codigo)
        for f in range(len(detalleCompras)):
            detalleCompras[f].pop(codigoIndex)

            print("Pedido eliminado exitosamente")
    else:
        print("El codigo ingresado no existe")

def pagoQRPichincha(i):
    textoPago = f"Datos del pago\n * Codigo del pedido: {detalleCompras[4][i]}\n * Pagofinal : $ {detalleCompras[5][i]}\n"

    codigoQr = pyqrcode.create(textoPago)
    nombreArchivo = "CodigoQr.png"
    codigoQr.png(nombreArchivo, scale=5)
    print("Codigo QR generado exitosamente")

def main():
    print("Bienvenido a TECHWORLD")
    opcion = menuopciones()
    while opcion != 5:
        if opcion == 1:
            ingresarpedido()
        elif opcion == 2:
            mostrarPedidos()
        elif opcion == 3:
            mostrarDetallePedido()
        elif opcion == 4:
            eliminarPedido()
        opcion = menuopciones()
        print("Gracias por usar el sistema")
main()