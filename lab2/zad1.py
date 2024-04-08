import socket
import struct
import time

def get_ntp_time(server='ntp.task.gda.pl'):
    try:
        # Utwórz gniazdo
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Ustal adres serwera NTP i port
        server_address = (server, 123)  # 123 to domyślny port NTP
        
        # Wyślij żądanie czasu do serwera NTP
        data = b'\x1b' + 47 * b'\0'
        sock.sendto(data, server_address)
        
        # Odbierz odpowiedź z serwera
        data, address = sock.recvfrom(1024)
        
        # Zamknij gniazdo
        sock.close()
       
        ntp_time = struct.unpack('!12I', data)[10] - 2208988800
        
        return ntp_time
    except Exception as e:
        print("Wystąpił błąd podczas pobierania czasu z serwera NTP:", e)
        return None

def main():
    # Pobranie czasu z serwera NTP
    ntp_time = get_ntp_time()
    
    if ntp_time is not None:
        print("Aktualny czas pobrany z serwera NTP:", time.ctime(ntp_time))
    else:
        print("Nie udało się pobrać czasu z serwera NTP.")

if __name__ == "__main__":
    main()
