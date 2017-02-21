#!/usr/bin/python3
import threading
import socket


HOST = "127.0.0.1"
PORT = 9999
SEP = b"\0"


def handle_client_input(sock):
    while True:
        try:
            data = input()
        except (KeyboardInterrupt, EOFError, ValueError):
            sock.close()
            exit(0)

        try:
            sock.send(data.encode("utf-8") + SEP)
        except IOError:
            return


def main():
    try:
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect((HOST, PORT))
    except socket.error:
        print("Can't connect to {}:{}".format(HOST, PORT))
        return
    threading.Thread(
        target=handle_client_input,
        args=[client_sock]
    ).start()

    accumulated_data = bytes()

    while True:
        data = client_sock.recv(1)
        if not data:
            print("Can't get data from server. Press Enter to escape.")
            break

        accumulated_data += data

        # show how accumulated_data grows.
        # print(accumulated_data)

        messages = []

        while True:
            if SEP in accumulated_data:
                msg, rest = accumulated_data.split(SEP, 1)
                accumulated_data = rest
                messages.append(msg)
            else:
                break

        for message in messages:
            print(message.decode())

    client_sock.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
