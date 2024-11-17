import customtkinter as tk
from customtkinter import filedialog


class GenConfig:
    def __init__(self):
        self.script = ""
        self.use_url = True
        self.url = ""
        self.video_path = ""
        self.voice_id = None
        self.speech_speed = 150
        self.speech_volume = 1


def select_file():
    file_path = filedialog.askopenfilename()
    global config
    config.video_path = file_path


def toggle_text():
    if use_url.get():
        button.pack_forget()
        url.pack(pady=20)
    else:
        url.pack_forget()
        button.pack(pady=20)


def set_speech_speed(value):
    global config
    config.speech_speed = value


def set_speed_volume(value):
    global config
    config.speech_volume = value


def set_voice(value):
    global config
    config.voice_id = value


config = GenConfig()

tk.set_appearance_mode('dark')
tk.set_default_color_theme('dark-blue')

root = tk.CTk()
root.geometry('500x350')
tabview = tk.CTkTabview(master=root)
tabview.pack(expand=True, fill='both')

script_frame = tabview.add('Script')
background_frame = tabview.add('Background')
voice_frame = tabview.add('Text-to-Speech')
generator_frame = tabview.add('Generate')

font_header = ('Roboto', 24)
font = ('Roboto', 12)

script_header = tk.CTkLabel(master=script_frame, text='Video Script', font=font_header)
script_header.pack(pady=20)
script_content = tk.CTkTextbox(master=script_frame, font=font, width=400, height=100)
script_content.pack()

url = tk.CTkEntry(master=background_frame, font=font)
button = tk.CTkButton(master=background_frame, text='Select File', command=select_file)

use_url = tk.BooleanVar()
url_switch = tk.CTkSwitch(master=background_frame, text='Use URL', font=font, variable=use_url, command=toggle_text,
                          onvalue=True, offvalue=False)
url_switch.pack(pady=20)

if use_url.get():
    button.pack_forget()
    url.pack(pady=20)
else:
    url.pack_forget()
    button.pack(pady=20)

tk.CTkLabel(master=voice_frame, text='Text-to-Speech', font=font_header).pack(pady=20)
tk.CTkLabel(master=voice_frame, text='Speech Speed', font=font).pack()
speech_speed = tk.CTkSlider(master=voice_frame, from_=50, to=200, command=set_speech_speed)
speech_speed.pack(pady=20)
tk.CTkLabel(master=voice_frame, text='Speech Volume', font=font).pack()
speech_volume = tk.CTkSlider(master=voice_frame, from_=0, to=1)
speech_volume.pack(pady=20)
# TODO: voice selection

config.use_url = use_url.get()
config.url = url.get()
config.script = script_content.get('1.0', 'end-1c')

# TODO: generation tab

root.mainloop()
