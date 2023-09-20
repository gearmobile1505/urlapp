import tkinter as tk
import pyshorteners

def shorten_url():
    url = entry.get()
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(url)
    result_label.config(text=f"Shortened URL: {short_url}")

# Create the main window
root = tk.Tk()
root.title("URL Shortener")

# Create widgets
label = tk.Label(root, text="Enter URL:")
entry = tk.Entry(root, width=40)
shorten_button = tk.Button(root, text="Shorten URL", command=shorten_url)
result_label = tk.Label(root, text="")

# Pack widgets
label.pack()
entry.pack()
shorten_button.pack()
result_label.pack()

root.mainloop()
