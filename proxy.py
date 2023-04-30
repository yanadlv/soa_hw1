import socket

HOST = "127.0.0.1"
PORT = 2000

# {format_name: port}
FORMATS = {"native": 2001, "xml": 2002, "json": 2003, "proto": 2004, "avro": 2005, "yaml": 2006, "msgpack": 2007}


def get_result(encoded_request):
    request = encoded_request.decode().split()
    if len(request) != 2 or request[0] != "get_result" or request[1].lower() not in FORMATS:
        return b'!INVALID REQUEST! Please try again\n'

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(b'!PERFORM COMPUTATION!\n', (HOST, FORMATS[request[1]]))
    result, address = s.recvfrom(2048)
    return result


def run():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))

        while True:
            request, address = s.recvfrom(2048)
            response = get_result(request)
            s.sendto(response, address)


if __name__ == "__main__":
    run()
