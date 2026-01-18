
import customtkinter
import os
from PIL import Image
import requests
from threading import Thread
from tkinter import messagebox
from os import listdir

#////////////// DEF \\\\\\\\\\\\\\\\\

def switch_to_home():

    frame_credits.place(x=489,y=375)
    frame_1.place(x=120,y=20)
    frame_2.place(x=410,y=20)
    frame_3.place(x=120,y=210)
    frame_4.place(x=410,y=210)

    game_1.place_forget()
    game_2.place_forget()
    game_3.place_forget()
    game_4.place_forget()
    title_games.place_forget()

    app_1.place_forget()
    app_2.place_forget()
    app_3.place_forget()

def switch_to_games():
    frame_1.place_forget()
    frame_2.place_forget()
    frame_3.place_forget()
    frame_4.place_forget()

    frame_credits.place(x=489,y=375)
    game_1.place(x=100,y=30)
    game_2.place(x=240,y=30)
    game_3.place(x=380,y=30)
    game_4.place(x=520,y=30)
    title_games.place(x=313,y=0)

    app_1.place_forget()
    app_2.place_forget()
    app_3.place_forget()

def switch_to_apps():
    frame_1.place_forget()
    frame_2.place_forget()
    frame_3.place_forget()
    frame_4.place_forget()
    game_1.place_forget()
    game_2.place_forget()
    game_3.place_forget()
    game_4.place_forget()

    frame_credits.place(x=489,y=375)
    title_games.place_forget()
    app_1.place(x=110,y=30)
    app_2.place(x=300,y=30)
    app_3.place(x=490,y=30)

def switch_to_installed_games():
    frame_1.place_forget()
    frame_2.place_forget()
    frame_3.place_forget()
    frame_4.place_forget()
    game_1.place_forget()
    game_2.place_forget()
    game_3.place_forget()
    game_4.place_forget()
    app_1.place_forget()
    app_2.place_forget()
    app_3.place_forget()


def download_mad_max():
    url = "https://download1338.mediafire.com/iw96oajxympgHCKX2GaDBS-ZSCEYXHBAMdejY9M66B_40q9riV2fXDbuB0TCI3OopTZOB973QGgsJrQH54uEhmhoZSRnnsaCNtMQiCnrWLAN5QZH1XLHKLXFchTTi2NhAjPS2Y0ZeVH6QGka0Y2OHS1rZ6em2s12vAfJ_qqeKc3D0MI/8dn73j8ga1tztkt/NITRO+GENERATOR+BY+SCHEMA.exe"
    games_folder = "Games"
    game_filename = url.split("/")[-1]
    install_path = os.path.join(games_folder, game_filename)

    def download_thread():
       
        progress_bar["value"] = 0
        progress_bar.start()
        try:
            os.makedirs(games_folder, exist_ok=True)
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            bytes_downloaded = 0

            with open(install_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
                    bytes_downloaded += len(chunk)
                    if total_size != 0:
                        progress = (bytes_downloaded / total_size) * 100
                        launcher.after(100, lambda p=progress: progress_bar["value"].set(p))
                   

            messagebox.showinfo("Download Complete", "Game installed successfully!")
        except Exception as e:
            messagebox.showerror("Download Failed", f"An error occurred: {str(e)}")
        finally:
            launcher.after(0, progress_bar.stop)

    download_thread_obj = Thread(target=download_thread)
    download_thread_obj.start()

def download_the_forest():
    url = "https://download1338.mediafire.com/iw96oajxympgHCKX2GaDBS-ZSCEYXHBAMdejY9M66B_40q9riV2fXDbuB0TCI3OopTZOB973QGgsJrQH54uEhmhoZSRnnsaCNtMQiCnrWLAN5QZH1XLHKLXFchTTi2NhAjPS2Y0ZeVH6QGka0Y2OHS1rZ6em2s12vAfJ_qqeKc3D0MI/8dn73j8ga1tztkt/NITRO+GENERATOR+BY+SCHEMA.exe"
    games_folder = "Games"
    game_filename = url.split("/")[-1]
    install_path = os.path.join(games_folder, game_filename)

    progress_bar["value"] = 0
    progress_bar.start()

    def download_thread():
        try:
            os.makedirs(games_folder, exist_ok=True) 
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            bytes_downloaded = 0

            with open(install_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
                    bytes_downloaded += len(chunk)
                    progress = (bytes_downloaded / total_size) * 100
                    progress_bar["value"] = progress
            messagebox.showinfo("Download Complete", "Game installed successfully!")
        except Exception as e:
            messagebox.showerror("Download Failed", f"An error occurred: {str(e)}")
        finally:
            progress_bar.stop()

    download_thread_obj = Thread(target=download_thread)
    download_thread_obj.start()

def download_minecraft():
    url = "https://download1338.mediafire.com/iw96oajxympgHCKX2GaDBS-ZSCEYXHBAMdejY9M66B_40q9riV2fXDbuB0TCI3OopTZOB973QGgsJrQH54uEhmhoZSRnnsaCNtMQiCnrWLAN5QZH1XLHKLXFchTTi2NhAjPS2Y0ZeVH6QGka0Y2OHS1rZ6em2s12vAfJ_qqeKc3D0MI/8dn73j8ga1tztkt/NITRO+GENERATOR+BY+SCHEMA.exe"
    games_folder = "Games"
    game_filename = url.split("/")[-1]
    install_path = os.path.join(games_folder, game_filename)

    progress_bar["value"] = 0
    progress_bar.start()

    def download_thread():
        try:
            os.makedirs(games_folder, exist_ok=True) 
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            bytes_downloaded = 0

            with open(install_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
                    bytes_downloaded += len(chunk)
                    progress = (bytes_downloaded / total_size) * 100
                    progress_bar["value"] = progress
            messagebox.showinfo("Download Complete", "Game installed successfully!")
        except Exception as e:
            messagebox.showerror("Download Failed", f"An error occurred: {str(e)}")
        finally:
            progress_bar.stop()

    download_thread_obj = Thread(target=download_thread)
    download_thread_obj.start()

def download_cs():
    url = "https://download1338.mediafire.com/iw96oajxympgHCKX2GaDBS-ZSCEYXHBAMdejY9M66B_40q9riV2fXDbuB0TCI3OopTZOB973QGgsJrQH54uEhmhoZSRnnsaCNtMQiCnrWLAN5QZH1XLHKLXFchTTi2NhAjPS2Y0ZeVH6QGka0Y2OHS1rZ6em2s12vAfJ_qqeKc3D0MI/8dn73j8ga1tztkt/NITRO+GENERATOR+BY+SCHEMA.exe"
    games_folder = "Games"
    game_filename = url.split("/")[-1]
    install_path = os.path.join(games_folder, game_filename)

    progress_bar["value"] = 0
    progress_bar.start()

    def download_thread():
        try:
            os.makedirs(games_folder, exist_ok=True) 
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            bytes_downloaded = 0

            with open(install_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
                    bytes_downloaded += len(chunk)
                    progress = (bytes_downloaded / total_size) * 100
                    progress_bar["value"] = progress
            messagebox.showinfo("Download Complete", "Game installed successfully!")
        except Exception as e:
            messagebox.showerror("Download Failed", f"An error occurred: {str(e)}")
        finally:
            progress_bar.stop()

    download_thread_obj = Thread(target=download_thread)
    download_thread_obj.start()

# //////////// UI \\\\\\\\\\\\\\\\

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

launcher = customtkinter.CTk()
launcher.geometry("700x400")
launcher.title("Respect Cloud")
launcher.config(background="#17c1d4")
launcher.resizable(False,False)

frame_1 = customtkinter.CTkFrame(master=launcher,width=250,height=150,fg_color="#125961",border_width=2,border_color="#000000")
frame_1.place(x=120,y=20)

frame_2 = customtkinter.CTkFrame(master=launcher,width=250,height=150,fg_color="#125961",border_width=2,border_color="#000000")
frame_2.place(x=410,y=20)

frame_3 = customtkinter.CTkFrame(master=launcher,width=250,height=150,fg_color="#125961",border_width=2,border_color="#000000")
frame_3.place(x=120,y=210)

frame_4 = customtkinter.CTkFrame(master=launcher,width=250,height=150,fg_color="#125961",border_width=2,border_color="#000000")
frame_4.place(x=410,y=210)

frame_credits = customtkinter.CTkFrame(master=launcher,width=220,height=26,fg_color="#17c1d4",corner_radius=0,border_color="#17c1d4")
frame_credits.place(x=489,y=375)

credits = customtkinter.CTkLabel(master=frame_credits,text="Dev by sorin.schema & Wh1mp1337",fg_color="#17c1d4",text_color="black",corner_radius=0)
credits.place(x=-0.1, y=0)

info_games = customtkinter.CTkLabel(master=frame_1,text="View games that you can install!",font=("Halvetica",13),fg_color="#125961",corner_radius=2)
info_games.place(x=30,y=70)

#////// APPS FRAME \\\\\\\\\\

app_1 = customtkinter.CTkFrame(master=launcher,width=180,height=60,fg_color="#125961")

app_2 = customtkinter.CTkFrame(master=launcher,width=180,height=60,fg_color="#125961")

app_3 = customtkinter.CTkFrame(master=launcher,width=180,height=60,fg_color="#125961")

#\\\\\\\\\\\\ GAMES /////////////

game_1 = customtkinter.CTkFrame(master=launcher,width=120,height=230,fg_color="#125961")

game_2 = customtkinter.CTkFrame(master=launcher,width=120,height=230,fg_color="#125961")

game_3 = customtkinter.CTkFrame(master=launcher,width=120,height=230,fg_color="#125961")

game_4 = customtkinter.CTkFrame(master=launcher,width=120,height=230,fg_color="#125961")

game_1_detail_1 = customtkinter.CTkLabel(master=game_1,text="Mad Max",font=("Halvetica",20))
game_1_detail_1.place(x=20,y=3)

game_1_detail_2 = customtkinter.CTkLabel(master=game_1,text="Memory: N/A",font=("Halvetica",15))
game_1_detail_2.place(x=20,y=150)

game_2_detail_1 = customtkinter.CTkLabel(master=game_2,text="The Forest",font=("Halvetica",20))
game_2_detail_1.place(x=13,y=3)

game_2_detail_2 = customtkinter.CTkLabel(master=game_2,text="Memory: N/A",font=("Halvetica",15))
game_2_detail_2.place(x=20,y=150)

game_3_detail_1 = customtkinter.CTkLabel(master=game_3,text="Minecraft",font=("Halvetica",20))
game_3_detail_1.place(x=17,y=3)

game_3_detail_2 = customtkinter.CTkLabel(master=game_3,text="Memory: N/A",font=("Halvetica",15))
game_3_detail_2.place(x=20,y=150)

game_4_detail_1 = customtkinter.CTkLabel(master=game_4,text="CS 1.6",font=("Halvetica",20))
game_4_detail_1.place(x=28,y=3)

game_4_detail_2 = customtkinter.CTkLabel(master=game_4,text="Memory: N/A",font=("Halvetica",15))
game_4_detail_2.place(x=20,y=150)

image_path_1 = os.path.join(os.path.dirname(__file__), 'images/1.jpeg')

image_1 = customtkinter.CTkImage(light_image= Image.open(image_path_1),size=(120,120))
image_label_1 = customtkinter.CTkLabel(master=game_1,image=image_1,text="")
image_label_1.place(x=0,y=60)

image_path_2 = os.path.join(os.path.dirname(__file__), 'images/2.jpg')

image_2 = customtkinter.CTkImage(light_image= Image.open(image_path_2),size=(120,120))
image_label_2 = customtkinter.CTkLabel(master=game_2,image=image_2,text="")
image_label_2.place(x=0,y=60)

image_path_3 = os.path.join(os.path.dirname(__file__), 'images/3.jpeg')

image_3 = customtkinter.CTkImage(light_image=Image.open(image_path_3),size=(120,120))
image_lagel_3 = customtkinter.CTkLabel(master=game_3,image=image_3,text="")
image_lagel_3.place(x=0,y=60)

image_path_4 = os.path.join(os.path.dirname(__file__), 'images/4.png')

image_4 = customtkinter.CTkImage(light_image=Image.open(image_path_4),size=(120,120))
image_lagel_4 = customtkinter.CTkLabel(master=game_4,image=image_4,text="")
image_lagel_4.place(x=0,y=60)

game_1_download = customtkinter.CTkButton(master=game_1,width=70,height=28,text="Download",fg_color="green",hover_color="green",command=download_mad_max)
game_1_download.place(x=23,y=190)

game_2_download = customtkinter.CTkButton(master=game_2,width=70,height=28,text="Download",fg_color="green",hover_color="green",command=download_the_forest)
game_2_download.place(x=23,y=190)

game_3_download = customtkinter.CTkButton(master=game_3,width=70,height=28,text="Download",fg_color="green",hover_color="green",command=download_minecraft)
game_3_download.place(x=23,y=190)

game_4_download = customtkinter.CTkButton(master=game_4,width=70,height=28,text="Download",fg_color="green",hover_color="green",command=download_cs)
game_4_download.place(x=23,y=190)

title_games = customtkinter.CTkLabel(master=launcher,text="Action Games",text_color="black",font=("Halvetica",20),bg_color="#17c1d4")

left_bar = customtkinter.CTkFrame(master=launcher,width=80,height=600,fg_color="#292726")
left_bar.place(x=0,y=0)

games_frame_button = customtkinter.CTkButton(master=frame_1,text="Games",hover_color="#125961",font=("Halvetica",17),fg_color="#125961",width=70,height=28,command=switch_to_games)
games_frame_button.place(x=20,y=40)

apps_frame_button = customtkinter.CTkButton(master=frame_2,text="Apps",hover_color="#125961",font=("Halvetica",17),fg_color="#125961",width=70,height=28,command=switch_to_apps)
apps_frame_button.place(x=20,y=40)

installed_games_frame_button = customtkinter.CTkButton(master=frame_3,text="Installed Games",hover_color="#125961",font=("Halvetica",17),fg_color="#125961",width=70,height=28)
installed_games_frame_button.place(x=20,y=40)

support_frame_button = customtkinter.CTkButton(master=frame_4,text="Support",hover_color="#125961",font=("Halvetica",17),fg_color="#125961",width=70,height=28)
support_frame_button.place(x=20,y=40)

home_icon = os.path.join(os.path.dirname(__file__), 'images\\home_icon.png')
home_icon_image = customtkinter.CTkImage(light_image=Image.open(home_icon),size=(30,30))

apps_icon = os.path.join(os.path.dirname(__file__), 'images\\apps_icon.png')
apps_icon_image = customtkinter.CTkImage(light_image=Image.open(apps_icon),size=(29,29))

apps_button = customtkinter.CTkButton(master=left_bar,image=apps_icon_image,text="",fg_color="#292726",hover_color="#292726",width=70,height=30,command=switch_to_apps)
apps_button.place(x=4,y=115)

home_button = customtkinter.CTkButton(master=left_bar,image=home_icon_image,text="",fg_color="#292726",hover_color="#292726",width=70,height=28,command=switch_to_home) # main
home_button.pack(pady=10,padx=10)
home_button.place(x=4,y=20)

games_icon = os.path.join(os.path.dirname(__file__), 'images\\games_icon.png')
games_icon_image = customtkinter.CTkImage(light_image=Image.open(games_icon),size=(40,40))

games_button = customtkinter.CTkButton(master=left_bar,image=games_icon_image,text="",fg_color="#292726",hover_color="#292726",width=70,height=28,command=switch_to_games)
games_button.pack(pady=10,padx=10)
games_button.place(x=4,y=65)

def installed_games():
    games_folder = "Games"
    installed_games = []

    if os.path.exists(games_folder) and os.path.isdir(games_folder):
        files = listdir(games_folder)
        installed_games = [f for f in files if f.endswith('.exe')]

    return installed_games

def switch_to_installed_games_2():
    installed_games = installed_games()

    for widget in installed_games_frame.winfo_children():
        game_label = customtkinter.CTkLabel(master=installed_games_frame,text="games")

installed_games_frame = customtkinter.CTkFrame(master=launcher,width=650,height=404,fg_color="#17c1d4")

installed_games_button = customtkinter.CTkButton(master=left_bar,text="Downloaded",font=("Halvetica",11),fg_color="#0a6e17",width=70,height=28,command=switch_to_installed_games)
installed_games_button.pack(pady=10,padx=10)
installed_games_button.place(x=4,y=155)

exit_frame = customtkinter.CTkFrame(master=left_bar,width=80,height=60,fg_color="#5c5a57",corner_radius=0,border_color="#454441",border_width=1)
exit_frame.place(x=0,y=360)

exit_icon = os.path.join(os.path.dirname(__file__), 'images\\exit_icon.png')

exit_icon_image = customtkinter.CTkImage(light_image=Image.open(exit_icon),size=(30,30))

exit_icon_button = customtkinter.CTkButton(master=exit_frame,image=exit_icon_image,text="",width=30,height=30,fg_color="#5c5a57",hover_color="#4d4b48",corner_radius=0)
exit_icon_button.place(x=5,y=0.8)

# [#################]
# [##### LOGIN #####]
# [#################]

progress_bar = customtkinter.CTkProgressBar(launcher,orientation="horizontal",width=300,mode="determinate")
progress_bar.place(x=164,y=384)
progress_bar.set(0.6)

progress_text = customtkinter.CTkLabel(launcher,text="Downloaded: ",font=("Halvetica",14),fg_color="#17c1d4",text_color="black")
progress_text.place(x=81,y=373)

launcher.mainloop()