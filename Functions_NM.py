import random
import time
import os
import RF24

# CONSTANTS 
import Constants_NM as CNTS

# IMPORTAR FUNCIONS DEFINIDES PER GRUP B --> ADAPTAR FUNCIONS FETES AMB LES SEVES FUNCIONS

# FUNCIONS AUXILIARS (ES POSARAN EN UN ALTRE DOCUMENT)

def is_usb_connected():
    usbpath = "/media/pi/" # Modificar per cada raspberry
    isconnected = False
    time.sleep(5)
    if len(os.listdir(os.path.dirname(usbpath))) != 0:
        usb = os.listdir(os.path.dirname(usbpath))[0]
        time.sleep(5)
        files = os.listdir(os.path.join(usbpath, usb))
        if len(files) != 0:
            isconnected = True
    return isconnected

def read_usb_file():
    usbpath = "/media/pi/" # Modificar per cada raspberry
    usb = os.listdir(os.path.dirname(usbpath))[0]
    files = os.listdir(os.path.join(usbpath, usb))
    filename = files[0]
    file = open(os.path.join(usbpath, usb, filename), "rb")
    data = file.read()
    file.close()
    return data

# Fer import de radio, mirar el self
# MIRAR COM S'ADAPTA AMB LES FUNCIONS DEL TEAM B
# UTILITZAR LES CONSTANTS DE RETRIES I TIMEOUTS
def send_hello(source_address, dest_address):
    responded = False
    hasData = False
    hadToken = False
    radio = RF24.RF24()
    radio.stopListening()
    # Part Team B
    hello_packet = HelloPacket(source_address, dest_address, CNTS.HELLO_PACKET)
    packetToSend = hello_packet.buildPacket()
    radio.write(packetToSend)
    # Part Team B
    # Esperar un temps???
    radio.startListening()
    if radio.available(): # buscar funcio per mirar si hi ha dades rebudes IMPORTANT!!! (potser es aquesta)
        # IMPLEMENTAR TIMEOUTS I RETRIES???
        responded = True
        rcvBytes = radio.read(32)
        rcvPacket = DataPacket()
        rcvPacket.parsePacket(rcvBytes)
        if rcvPacket.getTypePacket() == CNTS.HELLO_RESPONSE:
            hasData = rcvPacket.getField4() # No se si es modificarar el nom getField4()
            hadToken = rcvPacket.getField5() # No se si es modificarar el nom getField5()
    return responded, hasData, hadToken
  
# ACABAR FUNCIO
# MIRAR COM S'ADAPTA MAB LES FUNCIONS DEL TEAM B
def obtain_data_packets():
    filename = get_file()
    with open(filename,'rb') as f:
        ba = bytearray(f.read())
    os.system("sudo umount -l /mnt/USBDrive")
    to_send = create_list(number_of_files, ba)
    return to_send

# FER LA FUNCIO
def create_list(number_of_files, bytearray):
    return to_send

# Fer import de radio
# Declarar EOT
# Retorna true si la data s'ha enviat correctament
# MIRAR COM S'ADAPTA MAB LES FUNCIONS DEL TEAM B
# ACABAR FUNCIO
def send_data(myAddress, toAddress, data):
    # crear radio
    radio.openWritingPipe(pipesbytes)
    radio.powerUp()
    pack=0
    identifier = "010" #identifier Data packet
    for temp in to_send:
        for x in range(0,len(temp),31):
            data = identifier + pack
            aux = bytearray(data.to_bytes(1,'big')) + temp[x:x+31]
            while not(radio.write(aux)):    
                print("failed delivery ")
        pack+=1
    while not(radio.write(EOT)):    
        print("failed delivery " )
        time.sleep(0.01)

# Fer import de radio
# Declarar EOT
# MIRAR COM S'ADAPTA MAB LES FUNCIONS DEL TEAM B
# ACABAR FUNCIO
def wait_read_packets():
    finalData = ""
    radio.openReadingPipe(1, pipesbytes)
    radio.startListening()
    while EOT not in receivedPacket:
        if radio.available():
            receivedPacket = radio.read(32)
            header = receivedPacket[0]
            #Multiplico la header per 00001110 per quedarme amb els bits on hi ha la info del packet
            if (header&0x0E) = 0x00:
                return finalData, CNTS.HELLO_PACKET
            elif (header&0x0E) = 0x02:
                return finalData, CNTS.HELLO_RESPONSE
            elif (header&0x0E) = 0x04: 
                seqReceived = bool(header & 0x01)
                dec = header>>1
                if EOT not in receivedPacket:
                    if seq == seqReceived:
                        received[dec]=received[dec] + receivedPacket[1:32] 
                        seq=not seq    
            elif (header&0x0E) = 0x06:
                return finalData, CNTS.DATA_ACK
            elif (header&0x0E) = 0x08:
                return finalData, CNTS.TOKEN_PACKET
            elif (header&0x0E) = 0x0A:
                return finalData, CNTS.TOKEN_ACK 
    for dataReceived in received:
        finalData.extend(dataReceived)
    return finalData, CNTS.DATA_PACKET

# CANVIAR A GUARDAR A RASPBERRY
# ACABAR LA FUNCIO
def write_file(data):
    with open("/mnt/USBDrive/fileOutput.txt","wb") as f:
        f.write(data)

# #Functions to do:
# int read_token()
# send_token(address, token)
# send_token_ack() # no se si cal aquesta funcio
