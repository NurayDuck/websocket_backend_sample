from websocket import create_connection

ws = create_connection("ws://10.100.2.12:8000/ws/")

while True:
    msg = input('Enter a message: ')
    if msg == 'quit':        
        ws.close()
        break
    ws.send(msg)
    result =  ws.recv()
    print ('> ', result)