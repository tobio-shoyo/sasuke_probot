import nhentai
import os
import requests
import re
import img2pdf

from SaitamaRobot import pgram
from pyrogram import filters


@pgram.on_message(filters.command("nhentai"))
def hentai(_,message):
    hmm = message.text.replace(message.text.split(" ")[0] ,"")
    d = nhentai.get_doujin(int(hmm))

    i = 1
    os.mkdir(hmm)
    for x in d:
        url = x.url
        res = requests.get(url).content
        with open(f"{hmm}/{i}.jpg" , "wb") as f:
            f.write(res)
        i += 1
        file_paths = []
        for root, directories, files in os.walk(f"{hmm}"):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)

        file_paths.sort(key=lambda f: int(re.sub('\D', '', f)))
        with open(f"{hmm}.pdf" ,"wb") as f:
            f.write(img2pdf.convert(file_paths)) 
       

    pbot.send_document(message.chat.id , f"{hmm}.pdf")
    os.remove(f"{hmm}.pdf")
    os.system(f"rm -rf {hmm}")
