import socket
import time
import network
import _thread

#ssid = "Guillermo"
#password = "123456789"

#ssid = "Router P"
#password = "loco12345"

#ssid = "moto"
#password = "memoski7"

Running = True

ssid = "Pueblatec"
password = "Pueblatec1234"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    time.sleep(1)
print("Conexion establecida: ", wifi.ifconfig())

P1 = machine.Pin(0, machine.Pin.IN)
P2 = machine.Pin(1, machine.Pin.IN)
P3 = machine.Pin(2, machine.Pin.IN)
P4 = machine.Pin(3, machine.Pin.IN)
P5 = machine.Pin(4, machine.Pin.IN)
P6 = machine.Pin(5, machine.Pin.IN)

led1 = machine.Pin(16, machine.Pin.OUT)
led2 = machine.Pin(17, machine.Pin.OUT)
led3 = machine.Pin(18, machine.Pin.OUT)
led4 = machine.Pin(20, machine.Pin.OUT)
led5 = machine.Pin(19, machine.Pin.OUT)
led6 = machine.Pin(21, machine.Pin.OUT)
ledL = machine.Pin(14, machine.Pin.OUT)
ledV = machine.Pin(15, machine.Pin.OUT)


SERVER_IP = "192.168.18.234"

SERVER_PORT = 50000


def goalAnim():
    led1.value(1)
    time.sleep(0.1)
    led2.value(1)
    time.sleep(0.1)
    led3.value(1)
    time.sleep(0.1)
    led4.value(1)
    time.sleep(0.1)
    led5.value(1)
    time.sleep(0.1)
    led6.value(1)
    time.sleep(0.1)
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    led5.value(0)
    led6.value(0)
    time.sleep(0.5)
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(1)
    led5.value(1)
    led6.value(1)
    time.sleep(1)
    led6.value(0)
    time.sleep(0.1)
    led5.value(0)
    time.sleep(0.1)
    led4.value(0)
    time.sleep(0.1)
    led3.value(0)
    time.sleep(0.1)
    led2.value(0)
    time.sleep(0.1)
    led1.value(0)
    time.sleep(0.1)
    



def localLed():
    ledV.value(0)
    ledL.value(1)

def visitingLed():
    ledL.value(0)
    ledV.value(1)
    

def escucharPython():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 8080))
    s.listen(1)

    try:
        while True:
            conexion, direccion = s.accept()
            try:
                respuesta = conexion.recv(1024).decode()
                print(respuesta)
                if respuesta == "read":
                    conexion.close()
                    leerPaletas()
                    conexion.close()
                elif respuesta == "Lled":
                    conexion.close
                    localLed()
                elif respuesta == "Vled":
                    conexion.close()
                    visitingLed()
                elif respuesta == "goalA":
                    conexion.close()
                    goalAnim()
            except Exception as e:
                print("Error en la conexión:", e)
            finally:
                conexion.close()
    except Exception as e:
        print("Error al aceptar la conexión:", e)
    finally:
        s.close()


def leerPaletas():
    print("Leyendo paletas...")
    l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    l.connect((SERVER_IP, SERVER_PORT))
    start_time = time.time()
    try:
        while time.time() - start_time < 3:
            if P1.value() == 1:
                l.send(b"P1")
                print("P1 ENVIADA")
                l.close()
                break
            if P2.value() == 1:
                l.send(b"P2")
                print("P2 ENVIADA")
                l.close()
                break
            if P3.value() == 1:
                l.send(b"P3")
                print("P3 ENVIADA")
                l.close()
                break
            if P4.value() == 1:
                l.send(b"P4")
                print("P4 ENVIADA")
                l.close()
                break
            if P5.value() == 1:
                l.send(b"P5")
                print("P5 ENVIADA")
                l.close()
                break
            if P6.value() == 1:
                l.send("P6".encode())
                print("P6 ENVIADA")
                l.close()
                break
            time.sleep(0.01)
    except Exception as e:
        print("Error en conexión:", e)
    finally:
        l.close()
    escucharPython()

escucharPython()
