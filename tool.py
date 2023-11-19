# This is a pure work by Sudhanshu Ranjan
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk
import time

# Function to simulate data exchange and measure time
def perform_data_exchange():
    start_time = time.time()

    # Simulate data exchange between guest and host
    # We can replace this with your actual monitoring code

    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time

# Function to update the graphical elements
def update_graph():
    elapsed_time = perform_data_exchange()
    time_values.append(elapsed_time)

    # Update the graph with new data
    plt.clf()
    plt.plot(time_values)
    plt.xlabel('Data Exchange Iteration')
    plt.ylabel('Time (seconds)')
    plt.title('Data Exchange Performance')
    plt.draw()

# GUI using Tkinter
root = tk.Tk()
root.title("Security Tool")

# Create a button to trigger data exchange
exchange_button = tk.Button(root, text="Perform Data Exchange", command=update_graph)
exchange_button.pack()

# Matplotlib graph for data analysis
time_values = []
plt.ion()  # Turn on interactive mode for Matplotlib
fig = plt.figure(figsize=(6, 4))
plt.show()

# dialog box
root.mainloop()