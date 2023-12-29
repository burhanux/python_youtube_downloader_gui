import tkinter
import customtkinter
from pytube import YouTube

# Reference: https://youtu.be/NI9LXzo0UY0

def startDownload():
   try:
      ytLink = link.get()
      ytObject = YouTube(ytLink)
      video = ytObject.streams.get_highest_resolution()
      video.download()
   except:
      print("Youtube Link is invalid")
   print("Completed")

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40,textvariable=url_var)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run the app
app.mainloop()
