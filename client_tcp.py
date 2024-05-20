import socket

# принимаем адрес и порт сервера от пользователя
HOST_PORT = input("Введите адрес сервера в формате localhost:12345 -> ").split(":")
HOST = HOST_PORT[0]
PORT = int(HOST_PORT[1])

# создаем объект сокета
with socket.socket() as s:
    # подключаемся к серверу и отправляем сообщение
    s.connect((HOST, PORT))
    print("Успешное соединение с сервером ", HOST_PORT[0] + ":" + HOST_PORT[1])
    message = input(" -> ")

    # cоздаем цикл который проверяет введено ли ключевое слово при котором программа прекращает работу
    while message != "EXIT()":

        # отправляем данные на сервер
        s.send(message.encode("utf-8"))

        # принимаем сообщение от сервера
        data = s.recv(1024).decode("utf-8")

        print("Ответ от сервера", HOST_PORT[0] + ":" + HOST_PORT[1], ":", data)

        message = input(" -> ")

    # закрываем сокет
    s.close()
