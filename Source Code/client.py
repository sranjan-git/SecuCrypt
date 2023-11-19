import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk
import time
import socket
from scapy.all import sniff
from scapy.arch import get_if_list  # Import the get_if_list function

# List to store time measurements
time_values = []

# Function to perform data exchange and measure time
def perform_data_exchange():
    start_time = time.time()

    # Simulate data exchange between guest and host
    # actual monitoring code

    host = '192.168.56.1'  # Replace with the host machine's IP address
    port = 12345  # Use the same port as the server

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        data = input("Enter data to send: ")
        if not data:
            break  # No data entered
        client_socket.send(data.encode())  # Send data to the server

    client_socket.close()


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
root.title("Security Tool")

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