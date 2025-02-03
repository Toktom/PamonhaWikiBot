# -*- coding: utf-8 -*-
import locale
import os
from pamonha import save_image, get_file_page_url

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

fish = [
    "Lagostim",
    "Bodião",
    "Congro",
    "Solha",
    "Engulha",
    "Aratu",
    "Xaréu",
    "Anguila",
    "Carangazu",
    "Moreia de gruta",
]

fish_english = [
    "Heim crab",
    "Red-eye",
    "Dusk eel",
    "Giant flatfish",
    "Short-finned eel",
    "Web snipper",
    "Bouldabass",
    "Salve eel",
    "Blue crab",
    "Cave moray",
]

try:
    for i in range(len(fish)):
        page_name = "File:" + fish_english[i] + ".png"
        url = get_file_page_url("en-gb", page_name)
        print(page_name)
        name_to_save = "downloaded_images/" + fish[i] + ".png"
        if os.path.isfile(name_to_save) is False:
            save_image(name_to_save, url)
            print("File save in folder as: {}".format(name_to_save))
        else:
            print("File exists, skipping to next one in line!")
except Exception as e:
    print(e)
