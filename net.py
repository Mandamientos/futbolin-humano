import socket
import time
import network
import _thread

ssid = "Guillermo"
password = "123456789"

Running = True

#ssid = "Router P"
#password = "loco12345"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

Running = True

while not wifi.isconnected():
    time.sleep(1)
print("Conexion establecida: ", wifi.ifconfig())

P1 = machine.Pin(15, machine.Pin.IN)
P2 = machine.Pin(13, machine.Pin.IN)
P3 = machine.Pin(10, machine.Pin.IN)
P4 = machine.Pin(21, machine.Pin.IN)
P5 = machine.Pin(18, machine.Pin.IN)
P6 = machine.Pin(16, machine.Pin.IN)


# Configurar la dirección IP y el puerto del servidor

SERVER_IP = "192.168.0.5"

SERVER_PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 8080))
s.listen(1)

print(P1.value())

def escucharPython():
    global s
    while True:
        try:
            conexion, direccion = s.accept()
            respuesta = conexion.recv(1024).decode()
            print(respuesta)
            if respuesta == "testCircuit":
            #Conexion.sendall("Iniciado pa")
            #print("Mensaje enviado")
                _thread.start_new_thread(cuenta3, ())
                leerPaletas(conexion, direccion)
                break
            conexion.close()
            time.sleep(1)
        except:
            pass


def leerPaletas(conexion, direccion):
    while Running:
        try:
            l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            l.connect((SERVER_IP, SERVER_PORT))
            l.sendall("Hola Python".encode())
            l.close()
            time.sleep(1)
        except Exception as e:
            print("Error en conexión:", e)
            time.sleep(1)
    escucharPython()
    #while True:
        #try:
            #conexion.sendall("Hola Python =)")
            #print("Enviado")
            #if P1.value() == 1:
                #print("P1")
                #conexion.sendall("Paleta uno presionada")
            #if P2.value() == 1:
                #print("P2")
                #conexion.sendall("Paleta dos presionada")
            #if P3.value() == 1:
                #print("P3")
                #conexion.sendall("Paleta tres presionada")
            #if P4.value() == 1:
                #print("P4")
                #conexion.sendall("Paleta cuatro presionada")
            #if P5.value() == 1:
                #print("P5")
                #conexion.sendall("Paleta cinco presionada")
            #if P6.value() == 1:
                #print("P6")
                #conexion.sendall("Paleta seis presionada")
            #time.sleep(0.5)
        #except Exception as e:
            #print(e, "A")

def cuenta3():
    global Running
    time.sleep(3)
    Running = False
    time.sleep(1)


escucharPython()
s.close()


#while True:
    #try:
        #escucharPython()
    #except Exception as e:
        #pass
        #print(e, "A")
