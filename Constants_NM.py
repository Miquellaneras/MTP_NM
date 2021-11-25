import RF24

# CONSTANTS

HELLO_RETRIES = 4 # Mirar si s'ha de modificar
TOKEN_RETRIES = 4 # Mirar si s'ha de modificar
DATA_RETRIES = 4 # Mirar si s'ha de modificar
TIMEOUT = 0.001 # (en segons) Mirar si s'ha de modificar

NUM_NODES = 6

HELLO_PACKET = "000"
HELLO_RESPONSE = "001"
TOKEN_PACKET = "010"
DATA_PACKET = "100"
DATA_ACK_PACKET = "011"
TOKEN_ACK_PACKET = "101"

PIPES = [0x52, 0x78, 0x41, 0x41, 0x41]

# DECLARAR LES CONSTANTS DEL MODUL NRF24
DATARATE = RF24.RF24_1MBPS
POWERLEVEL = RF24.RF24_PA_MAX
CHANNEL = 6