import socket
import random
import time

target_ip = input("Inserisci l'IP della macchina target: ")
target_port = int(input("Inserisci la porta UDP della macchina target: "))
num_packets = int(input("Quanti pacchetti da 1KB vuoi simulare?: "))

packet_size = 1024  # 1 KB
packet_data = random._urandom(packet_size)  # Genera dati casuali da inviare

print(f"\n[SIMULAZIONE] Invio di {num_packets} pacchetti da 1KB verso {target_ip}:{target_port}\n")

for i in range(num_packets):
    print(f"[SIMULAZIONE] Pacchetto {i + 1}: inviato {len(packet_data)} byte a {target_ip}:{target_port}")
    time.sleep(0.1)  # Ritardo per simulare il tempo di invio

print("\n[SIMULAZIONE COMPLETATA] Nessun pacchetto reale è stato inviato.")