import json
import random
import time
import requests
import telebot
from humanfriendly import format_number
from bs4 import BeautifulSoup

TOKEN = "1015717313:AAE6zKWXzDezDUUYRfwwQPHNRT9uFpLHcQs"
myBot = telebot.TeleBot(TOKEN)

class mybot:
    def __init__(self):
        self.message

    apikey = "zAyMBQj0ogRbNcu1569fE929MTc2VJXjYCqzKWSVSlLm5txLRgOYBccFXGkrdfi2"

    userAgent = [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]

    @myBot.message_handler(commands=['start', 'help'])
    def start(message):
        responseText = "Halo @" + message.from_user.username + "\n"
        responseText += "╔══════ Command List ══════\n"
        responseText += "╠/start | Daftar Perintah Bot\n"
        responseText += "╠/speed | Cek Kecepatan Respon Bot\n"
        responseText += "╠/1cak | Konten 1Cak\n"
        responseText += "╠/iginfo [username] | Informasi Profil IG\n"
        responseText += "╠/wallpaper [keyword] | Mencari Wallpaper\n"
        responseText += "╠/searchyt [keyword] | Mencari Video YT Teratas\n"
        responseText += "╠/sendimage [url] | Bot Mengirim Gambar Sesuai URL\n"
        responseText += "╠/sendvideo [url] | Bot Mengirim Video Sesuai URL\n"
        responseText += "╠/sendaudio [url] | Bot Mengirim Audio Sesuai URL\n"
        responseText += "╠/artinama [nama] | Cek Arti Nama\n"
        responseText += "╠/checkdate [dd-mm-yyyy] | Cek Tanggal Lahir\n"
        responseText += "╠/searchimage [keyword] | Mencari Gambar dari Pexels\n"
        responseText += "╠/ramalanzodiak [zodiak]\n"
        responseText += "╚═══ /creator : @rafizadanly ═════"
        myBot.reply_to(message, responseText)

    @myBot.message_handler(commands='speed')
    def speed(message):
        start = time.time()
        myBot.send_message(message.chat.id, "Start Checking Speed")
        elapsed_time = time.time() - start
        myBot.reply_to(message, "Response Speed\n" + format(str(elapsed_time)) + " Seconds")

    @myBot.message_handler(commands='creator')
    def creator(message):
        myBot.send_contact(message.chat.id, "6285894015326", "My Creator 👍")

    @myBot.message_handler(commands='sendimage')
    def sendImage(message):
        sep = message.text.split(" ")
        query = message.text.replace(sep[0] + " ", "")
        if query != "/sendimage":
            myBot.send_message(message.chat.id, "Mohon Tunggu Sebentar...")
            try:
                myBot.send_photo(message.chat.id, query,
                                 "Halo @" + message.from_user.username + " ini hasil gambar dari url " + query)
            except:
                myBot.reply_to(message, "Format URL salah, harus terdapat ekstensi gambar seperti jpg atau semacamnya")
        else:
            myBot.reply_to(message, "Format URL salah, harus terdapat ekstensi gambar seperti jpg atau semacamnya")

    @myBot.message_handler(commands='sendvideo')
    def sendVideo(message):
        sep = message.text.split(" ")
        query = message.text.replace(sep[0] + " ", "")
        if query != "/sendvideo":
            myBot.send_message(message.chat.id, "Mohon Tunggu Sebentar...")
            try:
                myBot.send_video(message.chat.id, query,
                                 "Halo @" + message.from_user.username + " ini hasil video dari url " + query)
            except:
                myBot.reply_to(message, "Format URL salah, harus terdapat ekstensi gambar seperti mp4 atau semacamnya")
        else:
            myBot.reply_to(message, "Format URL salah, harus terdapat ekstensi gambar seperti mp4 atau semacamnya")

    @myBot.message_handler(commands='sendaudio')
    def sendAudio(message):
        sep = message.text.split(" ")
        query = message.text.replace(sep[0] + " ", "")
        if query != "/sendaudio":
            myBot.send_message(message.chat.id, "Mohon Tunggu Sebentar...")
            try:
                myBot.send_audio(message.chat.id, query,
                                 "Halo @" + message.from_user.username + " ini hasil audio dari url " + query)
            except:
                myBot.reply_to(message, "Format URL salah, harus terdapat ekstensi gambar seperti mp3 atau semacamnya")
        else:
            myBot.reply_to(message, "Format URL salah, harus terdapat ekstensi gambar seperti mp3 atau semacamnya")

    @myBot.message_handler(commands='checkdate')
    def checkDate(message):
        sep = message.text.split(" ")
        query = message.text.replace(sep[0] + " ", "")
        if query != "/checkdate":
            myBot.send_message(message.chat.id, "Mohon Tunggu Sebentar...")
            api_url = "https://mnazria.herokuapp.com/api/checkdate?tanggal-bulan-tahun="+query
            req_data = requests.get(api_url)
            result = req_data.json()
            responseText = "╔═══════[ "+ query +" ]═══════\n"
            responseText += "╠ Zodiak : " + result['zodiak'] + "\n"
            responseText += "╠ Tgl Lahir : " + result['date-of-birth'] + "\n"
            responseText += "╠ Umur : " + result['age'] + "\n"
            responseText += "╠ Ulang Tahun : " + result['birthday'] + "\n"
            responseText += "╚═══════════════════════════════"
            myBot.reply_to(message, responseText)

    @myBot.message_handler(commands='searchimage')
    def searchImage(message):
        sep = message.text.split(" ")
        query = message.text.replace(sep[0] + " ", "")
        if query != "/searchimage":
            myBot.send_message(message.chat.id, "Mohon Tunggu Sebentar...")
            api_url = "https://mnazria.herokuapp.com/api/imagehd?search="+query.replace(" ", "+")
            req_data = requests.get(api_url)
            result = req_data.json()
            try:
                responseText = "════════[ More Image URL ]═══════\n"
                num = 1
                for i in result:
                    responseText += str(num) + ". " + i + "\n"
                    responseText += "══════════════════════════\n"
                    num += 1
                myBot.send_photo(message.chat.id, result[0], "Halo @" + message.from_user.username + " ini hasil pencarian gambar " + query)
                myBot.send_message(message.chat.id, responseText)
            except:
                myBot.send_message(message.chat.id, "Halo @" + message.from_user.username + " Maaf gambar yang anda cari tidak ditemukan")
        else:
            myBot.reply_to(message, "Isikan keyword untuk mencari gambar \nContoh : /searchimage workout")

    @myBot.message_handler(commands='artinama')
    def artiNama(message):
        sep = message.text.split(" ")
        query = message.text.replace(sep[0] + " ", "")
        if query != "/artinama":
            myBot.send_message(message.chat.id, "Mohon Tunggu Sebentar...")
            api_url = "https://mnazria.herokuapp.com/api/arti?nama=" + query.replace(" ", "+")
            req_data = requests.get(api_url)
            result = req_data.json()
            res = result["result"].split(",");
            myBot.reply_to(message, result["result"].replace(res[0] + ", ", ""))
        else:
            myBot.reply_to(message, "Isikan Nama \nContoh : /artinama zadd bot")

    @myBot.message_handler(commands='wallpaper')
    def wallpaper(message):
        sep = message.text.split(" ")
        query = message.text.replace(sep[0] + " ", "")
        if query != "/wallpaper":
            myBot.send_message(message.chat.id, "Mohon Tunggu Sebentar...")
            api_url = "https://beta.moe.team/api/wallpaper/?apikey=" + mybot.apikey + "&q=" + query.replace(" ", "+")
            req_data = requests.get(api_url)
            result = req_data.json()
            if result["code"] == 200:
                responseText = "════════[ More Image URL ]═══════\n"
                num = 1
                for i in result["result"]:
                    responseText += str(num) + ". " + i + "\n"
                    responseText += "══════════════════════════\n"
                    num += 1
                myBot.send_photo(message.chat.id, result["result"][0],
                                 "Halo @" + message.from_user.username + " ini hasil pencarian wallpaper " + query)
                myBot.send_message(message.chat.id, responseText)
            else:
                myBot.reply_to(message, "Terjadi Kesalahan, Coba lagi Nanti")
        else:
            myBot.reply_to(message, "Isikan keyword untuk mencari wallpaper \nContoh : /wallpaper game")

    @myBot.message_handler(commands='1cak')
    def meme(message):
        myBot.send_message(message.chat.id, "Mohon Tunggu Sebentar...")
        api_url = "http://beta.moe.team/api/1cak?apikey=" + mybot.apikey
        req_data = requests.get(api_url)
        result = req_data.json()
        if result["code"] == 200:
            title = result["result"]["title"]
            path = result["result"]["image"]
            myBot.send_photo(message.chat.id, path, "Judul : " + title)
        else:
            myBot.reply_to(message, "Terjadi Kesalahan, Coba lagi Nanti")

    @myBot.message_handler(commands='ramalanzodiak')
    def ramalanzodiak(message):
        sep = message.text.split(" ")
        query = message.text.replace(sep[0] + " ", "")
        if query != "/ramalanzodiak":
            myBot.send_message(message.chat.id, "Mohon Tunggu Sebentar...")
            api_url = "http://beta.moe.team/api/zodiak?apikey=" + mybot.apikey + "&q=" + query
            req_data = requests.get(api_url)
            result = req_data.json()
            if result["code"] == 200:
                myBot.reply_to(message, result["result"])
            else:
                myBot.reply_to(message, "Terjadi Kesalahan, Coba lagi Nanti")
        else:
            myBot.reply_to(message, "Isikan Nama Zodiak \nContoh : /ramalanzodiak leo")

    @myBot.message_handler(commands='iginfo')
    def instagramInfo(message):
        sep = message.text.split(" ")
        query = message.text.replace(sep[0] + " ", "")
        if query != "/iginfo":
            myBot.send_message(message.chat.id, "Mohon Tunggu Sebentar...")
            with requests.session() as web:
                web.headers["User-Agent"] = random.choice(mybot.userAgent)
                r = web.get("https://www.instagram.com/{}/?__a=1".format(query))
                try:
                    data = json.loads(r.text)
                    ret_ = "╔══[ Profile Instagram ]"
                    ret_ += "\n╠ Nama : {}".format(str(data["graphql"]["user"]["full_name"]))
                    ret_ += "\n╠ Username : {}".format(str(data["graphql"]["user"]["username"]))
                    ret_ += "\n╠ Bio : {}".format(str(data["graphql"]["user"]["biography"]))
                    ret_ += "\n╠ Pengikut : {}".format(
                        format_number(data["graphql"]["user"]["edge_followed_by"]["count"]))
                    ret_ += "\n╠ Diikuti : {}".format(format_number(data["graphql"]["user"]["edge_follow"]["count"]))
                    if data["graphql"]["user"]["is_verified"] == True:
                        ret_ += "\n╠ Verifikasi : Sudah"
                    else:
                        ret_ += "\n╠ Verifikasi : Belum"
                    if data["graphql"]["user"]["is_private"] == True:
                        ret_ += "\n╠ Akun Pribadi : Iya"
                    else:
                        ret_ += "\n╠ Akun Pribadi : Tidak"
                    ret_ += "\n╠ Total Post : {}".format(
                        format_number(data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]))
                    ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(query)
                    path = data["graphql"]["user"]["profile_pic_url_hd"]
                    myBot.send_photo(message.chat.id, path, query + " Instagram Profile Picture")
                    myBot.reply_to(message, str(ret_))
                except:
                    myBot.reply_to(message, "Pengguna Tidak Ditemukan")
        else:
            myBot.reply_to(message, "Isikan Username Instagram.\nContoh: /iginfo username")

    @myBot.message_handler(commands='searchyt')
    def searchYoutube(message):
        sep = message.text.split(" ")
        query = message.text.replace(sep[0] + " ", "")
        if query != "/searchyt":
            myBot.send_message(message.chat.id, "Mohon Tunggu Sebentar...")
            params = {"search_query": query.replace(" ", "+")}
            with requests.session() as web:
                web.headers["User-Agent"] = random.choice(mybot.userAgent)
                r = web.get("https://www.youtube.com/results", params=params)
                soup = BeautifulSoup(r.content, "html5lib")
                ret_ = "╔══[ Youtube Result ]"
                datas = []
                for data in soup.select(".yt-lockup-title > a[title]"):
                    if "&lists" not in data["href"]:
                        datas.append(data)
                for data in datas:
                    ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                    ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                ret_ += "\n╚══[ Total {} ]".format(len(datas))
                myBot.reply_to(message, str(ret_))
        else:
            myBot.reply_to(message, "Isikan Keyword yang ingin dicari\nContoh: /searchyt music")

print("-- Bot sedang berjalan --")
myBot.polling(none_stop=True)