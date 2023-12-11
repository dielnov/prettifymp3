# Written For Fun By Dielnov Muchati(https://github.com/dielnov)
#iCode4Fun
import customtkinter as ctk
import tkinter as tk
import os

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

mp3_file_list = []
mp3_file_list_index = 0
mp3_file_list_length = 0
album_artist_name = ''
count = 0
state = 0

def on_return_key(event):
    global state
    state = 1
    rename_mp3_file()


def state_selector():
    global state
    if state == 0:
        state = 1
    else:
        state = 0

def list_length(some_list):
    some_list = some_list
    count_i = 0
    for f in some_list:
        count_i = count_i + 1

    return count_i

def select_folder():
    global album_artist_name, state
    album_directory = tk.filedialog.askdirectory()
    os.chdir(album_directory)

    album_artist_dialog = ctk.CTkInputDialog(text="Enter Album Artist Name:", title="Album Artist Name")

    album_artist_name = album_artist_dialog.get_input() # waits for input
    state = 0

    for f in os.listdir():
        mp3_file_list.append(f)

def rename_mp3_file():
    global count
    global state
    mp3_file_list_length = list_length(mp3_file_list)
    if mp3_file_list_length > 0:
        if count < mp3_file_list_length:
            f = mp3_file_list[count]
            fn, fx = os.path.splitext(f)
            if fx == '.mp3':
                if state == 0:
                    entry.delete(0,ctk.END)
                    entry.insert(0,str(fn))
                    state_selector()
                else:
                    new_song_title = entry.get()
                    new_file_name = '{} - {}.mp3'.format(album_artist_name,new_song_title)
                    os.rename(f,new_file_name)
                    entry.delete(0,ctk.END)
                    if count + 1 < mp3_file_list_length:
                        entry.insert(0,str(os.path.splitext(mp3_file_list[count+1])[0]))
                    else:
                        entry.insert(0,"NO MORE mp3 FILES TO RENAME!!!")
                    result_label = ctk.CTkLabel(scf, text=new_file_name, font=ctk.CTkFont(size=12,weight="bold"))
                    result_label.pack()
                    count = count + 1

root = ctk.CTk()
root.geometry("720x640")
root.title("PRETIFFY mp3")

lb = ctk.CTkLabel(root, text="PRETIFFY mp3 FILES", font=ctk.CTkFont(size=30,weight="bold"))
lb.pack(padx=20, pady=(20,0))

lb2 = ctk.CTkLabel(root, text="By Dielnov Muchati", font=ctk.CTkFont(size=10,weight="normal"))
lb2.pack()

scf = ctk.CTkScrollableFrame(root, width=640, height=420)
scf.pack()

entry = ctk.CTkEntry(scf, placeholder_text="NEW MP3 FILE TITLE HERE")
entry.bind('<Return>',command=on_return_key)
entry.pack(fill="x")

save_btn = ctk.CTkButton(root, text="SELECT ALBUM FOLDER", width=500, command=select_folder)
save_btn.pack(pady=20)

rename_btn = ctk.CTkButton(root, text="RENAME mp3 FILE", width=500, command=rename_mp3_file)
rename_btn.pack()

root.mainloop()
# Written For Fun By Dielnov Muchati(https://github.com/dielnov)
#iCode4Fun