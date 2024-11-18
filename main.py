import customtkinter as tk
from customtkinter import filedialog
import tts
import generator


class GenConfig:
    def __init__(self):
        self.script = ""
        self.use_url = True
        self.url = ""
        self.video_path = ""
        self.voice = None
        self.speech_speed = 150
        self.speech_volume = 1
        self.output_path = ""

    def __str__(self):
        return f"Script: {self.script}\n" \
               f"Use URL: {self.use_url}\n" \
               f"URL: {self.url}\n" \
               f"Video Path: {self.video_path}\n" \
               f"Speech Speed: {self.speech_speed}\n" \
               f"Speech Volume: {self.speech_volume}\n" \
               f"Output Path: {self.output_path}"


def select_file():
    global file_path
    file_path = filedialog.askopenfilename()
    print(file_path)


def toggle_text():
    if use_url.get():
        button.pack_forget()
        url.pack(pady=20)
    else:
        url.pack_forget()
        button.pack(pady=20)


def init_generation():
    config = GenConfig()

    config.use_url = use_url.get()
    config.url = url.get()
    config.video_path = file_path
    config.script = script_content.get('1.0', 'end-1c')
    config.speech_speed = speech_speed.get()
    config.speech_volume = speech_volume.get()
    config.voice = voice.get()
    config.output_path = output.get()
    generator.generate(config)


tk.set_appearance_mode('dark')
tk.set_default_color_theme('dark-blue')
font_header = ('Roboto', 24)
font = ('Roboto', 12)
file_path = ''

root = tk.CTk()
root.geometry('500x350')
tabview = tk.CTkTabview(master=root)
tabview.pack(expand=True, fill='both')

script_frame = tabview.add('Script')
background_frame = tabview.add('Background')
voice_frame = tabview.add('Text-to-Speech')
generator_frame = tabview.add('Generate')

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
speech_speed = tk.CTkSlider(master=voice_frame, from_=50, to=250)
speech_speed.pack(pady=20)
tk.CTkLabel(master=voice_frame, text='Speech Volume', font=font).pack()
speech_volume = tk.CTkSlider(master=voice_frame, from_=0, to=1)
speech_volume.pack(pady=20)
voices = tts.get_voices()
voice_options = [voice.name for voice in voices]
voice = tk.CTkComboBox(master=voice_frame, values=voice_options, font=font)
voice.pack(pady=20)

tk.CTkLabel(master=generator_frame, text='Output Path', font=font).pack(pady=20)
output = tk.CTkEntry(master=generator_frame, font=font)
output.pack(pady=20)
(tk.CTkButton(master=generator_frame, text='Generate', font=font_header, command=init_generation)
 .pack(pady=50))

root.mainloop()
