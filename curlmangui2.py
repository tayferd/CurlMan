import subprocess
import tkinter as tk
from tkinter import filedialog
import subprocess
import tkinter as tk
from tkinter import filedialog
import webbrowser  # Added import for webbrowser
def execute_curl_command():
    url = entry_url.get()
    method = var_method.get()
    data = entry_data.get()
    headers = entry_headers.get()

    curl_command = f'curl -X {method} {url}'
    if data:
        curl_command += f" -d '{data}'"
    if headers:
        curl_command += f" -H '{headers}'"

    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result.stdout)
    else:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result.stderr)

def save_request():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            file.write(f"URL: {entry_url.get()}\n")
            file.write(f"Method: {var_method.get()}\n")
            file.write(f"Data: {entry_data.get()}\n")
            file.write(f"Headers: {entry_headers.get()}\n")
            file.write("Response:\n")
            response_text = output_text.get("1.0", tk.END)  # Retrieve the text from the output_text widget
            file.write(response_text)  # Write the response to the file


def load_request():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("URL:"):
                    entry_url.delete(0, tk.END)
                    entry_url.insert(tk.END, line.strip().split(": ", 1)[1])
                elif line.startswith("Method:"):
                    var_method.set(line.strip().split(": ", 1)[1])
                elif line.startswith("Data:"):
                    entry_data.delete(0, tk.END)
                    entry_data.insert(tk.END, line.strip().split(": ", 1)[1])
                elif line.startswith("Headers:"):
                    entry_headers.delete(0, tk.END)
                    entry_headers.insert(tk.END, line.strip().split(": ", 1)[1])

# Create the tkinter window and other widgets...
# (Same as before)
window = tk.Tk()
window.title("cURL Request Maker")

# URL input
label_url = tk.Label(window, text="URL:")
label_url.grid(row=0, column=0, sticky="w")
entry_url = tk.Entry(window, width=50)
entry_url.grid(row=0, column=1, columnspan=3)

# Method selection
label_method = tk.Label(window, text="Method:")
label_method.grid(row=1, column=0, sticky="w")
var_method = tk.StringVar(value="GET")
method_options = ["GET", "POST", "PUT", "DELETE"]
method_menu = tk.OptionMenu(window, var_method, *method_options)
method_menu.grid(row=1, column=1)

# Data input
label_data = tk.Label(window, text="Data:")
label_data.grid(row=2, column=0, sticky="w")
entry_data = tk.Entry(window, width=50)
entry_data.grid(row=2, column=1, columnspan=3)

# Headers input
label_headers = tk.Label(window, text="Headers:")
label_headers.grid(row=3, column=0, sticky="w")
entry_headers = tk.Entry(window, width=50)
entry_headers.grid(row=3, column=1, columnspan=3)

# Button to execute the request
button_execute = tk.Button(window, text="Execute Request", command=execute_curl_command)
button_execute.grid(row=4, column=0, columnspan=4, pady=10)

# Output text area
output_text = tk.Text(window, height=10, width=60)
output_text.grid(row=5, column=0, columnspan=4, padx=10, pady=10)



# Button to save the request
button_save = tk.Button(window, text="Save Request", command=save_request)
button_save.grid(row=6, column=0)

# Button to load a saved request
button_load = tk.Button(window, text="Load Request", command=load_request)
button_load.grid(row=6, column=1)



def execute_curl_command():
    url = entry_url.get()
    method = var_method.get()
    data = entry_data.get()
    headers = entry_headers.get()

    curl_command = f'curl -X {method} {url}'
    if data:
        curl_command += f" -d '{data}'"
    if headers:
        curl_command += f" -H '{headers}'"

    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result.stdout)
    else:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, result.stderr)

def save_request():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "w") as file:
            file.write(f"URL: {entry_url.get()}\n")
            file.write(f"Method: {var_method.get()}\n")
            file.write(f"Data: {entry_data.get()}\n")
            file.write(f"Headers: {entry_headers.get()}\n")
            file.write("Response:\n")
            response_text = output_text.get("1.0", tk.END)
            file.write(response_text)

def load_request():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("URL:"):
                    entry_url.delete(0, tk.END)
                    entry_url.insert(tk.END, line.strip().split(": ", 1)[1])
                elif line.startswith("Method:"):
                    var_method.set(line.strip().split(": ", 1)[1])
                elif line.startswith("Data:"):
                    entry_data.delete(0, tk.END)
                    entry_data.insert(tk.END, line.strip().split(": ", 1)[1])
                elif line.startswith("Headers:"):
                    entry_headers.delete(0, tk.END)
                    entry_headers.insert(tk.END, line.strip().split(": ", 1)[1])

def open_url():
    webbrowser.open(entry_url.get())  # Function to open URL in the default web browser

# Create the tkinter window and other widgets...

# Layout setup as before, including other widgets and buttons...

# Button to open URL in browser
button_open_url = tk.Button(window, text="Open URL in Browser", command=open_url)
button_open_url.grid(row=7, column=0, columnspan=4, pady=10)  # Added button to open URL




window.mainloop()