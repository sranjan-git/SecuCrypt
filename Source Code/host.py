import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk
import time
import socket
from scapy.all import sniff
from scapy.arch import get_if_list  # Import the get_if_list function
from cryptography.fernet import Fernet



# List to store time measurements
time_values = []


# Function to perform data exchange and measure time
def perform_data_exchange():
    start_time = time.time()

    # Simulate data exchange between guest and host
    # actual monitoring code

    

    host = '192.168.56.1'  # Listen on all available network interfaces
    port = 12345  # Use a free port

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for one incoming connection

    print(f"Waiting for a connection on {host}:{port}...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    while True:
        data = client_socket.recv(1024)  # Receive data from the client
        if not data:
            break  # No more data received

        # Encrypt the data before sending
        encrypted_data = cipher_suite.encrypt(data)
        print(f"Received (Encrypted): {encrypted_data}")

        # Decrypt the data when received
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        print(f"Plain Text (Decrypted): {decrypted_data.decode()}")

    client_socket.close()
    server_socket.close()

    # Generate an AES secret key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to sniff packets
def start_sniffing():
    # Define a packet capture function
    def packet_capture(packet):
        # Process captured packets here
        pass

    # Get the first available network interface
    iface = get_if_list()[0]

    

    # Start packet sniffing on the selected interface for a specified duration
    sniff(iface=iface, prn=packet_capture, timeout=10)  # Sniff packets for 10 seconds

# Function to update the graphical elements
def update_graph():
    perform_data_exchange()
    elapsed_time = time_values[-1]

    # Update the graph with new data
    plt.clf()
    plt.plot(time_values)
    plt.xlabel('Data Exchange Iteration')
    plt.ylabel('Time (seconds)')
    plt.title('Data Exchange Performance')
    plt.draw()

    # Compute and display the time mean
    mean_time = sum(time_values) / len(time_values)
    mean_label.config(text=f'Mean Time: {mean_time:.2f} seconds')

# Create a GUI using Tkinter
root = tk.Tk()
root.title("SecuCrypt")

# Create a button to perform data exchange
exchange_button = tk.Button(root, text="Perform Data Exchange", command=update_graph)
exchange_button.pack()

# Create a button to start packet sniffing
sniff_button = tk.Button(root, text="Start Packet Sniffing", command=start_sniffing)
sniff_button.pack()

# Create a Matplotlib graph for data analysis
plt.ion()  # Turn on interactive mode for Matplotlib
fig = plt.figure(figsize=(6, 4))
plt.show()

# Create a label for displaying the mean time
mean_label = ttk.Label(root, text="")
mean_label.pack()

# Create the main dialog box
root.mainloop()
