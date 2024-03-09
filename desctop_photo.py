#hi =)
from tkinter import *
import ctypes
from tkinter import ttk
import os

index_current_photo = 0
window = Tk()
window.title("Выбор изображения рабочего стола")
window.resizable = (False, False)
window.geometry("800x680")

def mas_png_in_folder(folder_path):
    mas = []
    for file in os.listdir(folder_path):
        if file.endswith(".png"):
        	mas.append(file)
    return mas

def get_names_from_photo_format(list_photo):
    names = []
    for photo in list_photo:
        names.append(photo.split(".")[0])
    return names

def change_desktop_photo():
	image_path = path_photo + list_photo[index_current_photo] 
	SPI_SETDESKWALLPAPER = 20
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

def create_obj_photo(path, list_photo, width, height):
	objs_photos = []
	for photo in list_photo:
		obj_photo = PhotoImage(file=path_photo + photo)
		zoom_width = obj_photo.width() // width
		zoom_height = obj_photo.height() // height
		objs_photos.append(obj_photo.subsample(zoom_width, zoom_height))
	return objs_photos

def selected(event):
    global index_current_photo
    name_photo = combobox.get()
    index_current_photo = names.index(name_photo)
    current_photo = objs_photos[index_current_photo]
    lbl.config(image=current_photo)

path_photo = f"{os.getcwd()}\\Photo\\"
list_photo = mas_png_in_folder(path_photo)
names = get_names_from_photo_format(list_photo)
objs_photos = create_obj_photo(path_photo, list_photo, 580, 400)


lbl = Label(window, image=objs_photos[index_current_photo])
lbl.place(x=0, y=0)

photo_var = StringVar(value=names[0])
combobox = ttk.Combobox(values=names, textvariable=photo_var)
combobox.bind("<<ComboboxSelected>>", selected)

combobox.place(x=30, y=600)


btn = Button(master=window, background="red", text="поменять фото рабочего стола", command=change_desktop_photo)
btn.place(x = 300, y = 600)
window.mainloop()



