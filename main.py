import requests
import telebot 
bot = telebot.TeleBot("6794649818:AAHfzQYemO2QmSnZF4boHzSyxZ329sSf-5s")
@bot.message_handler(commands=["start"])
def s(message):
    bot.reply_to(message ,'''
    اهلا بك في هذا البوت ❤✅
    ارسل اسمك وانتظر صور التهاني 🫶🏻🎁 بحقوقك 
    ~ مطور البوت : @altaee_z
    ♡ قناة المطور : @my00002
    ''')
@bot.message_handler(func=lambda message:True)
def ss(message):
    mess = message.text
    ra = ['157', '190', '188', '196', '200', '202', '211', '576', '581', '582', '598', '608', '612', '611', '613', '614', '672', '615', '674', '673', '676', '675', '678', '677']
    for pe in ra:
        url = "https://card.tqniait.com/card"
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "ar-US,ar;q=0.9,en-US;q=0.8,en;q=0.7,ku;q=0.6",
            "Cookie": "XSRF-TOKEN=eyJpdiI6ImxPQzgxSXBuT0haTEdrYnd4M2lmTUE9PSIsInZhbHVlIjoiTE1TckFKMXpWcDR2cCtVUnoxVGVoOGRhNjlKajVIYmFINEdzb1wvdEw1VElVdTdYdnpDcTFaODY3U1Z1WXRDY0EiLCJtYWMiOiI3ZjgyY2UyNmUzYzliNjNmN2Q2MjFlNGFmMmY2MWRhZDAwY2Q5ZjhlYjA0YzEzM2UyMmVlMGQxMmRjZjRhNjc1In0%3D; card_session=eyJpdiI6IkJMbUVSSW1EMWRFU2FUd250QWM5XC93PT0iLCJ2YWx1ZSI6InFvVlRNamVibjk0SGxHQm1hOTRxbUFqNnZjdGdDWkFqMThCaUtIanlcLzZuaFwvMXZcL0l2cnFIajVTN0VIbE42eUUiLCJtYWMiOiI5ZGY2M2RmNGZlNWVlNTQ0MDAyZjE1M2E4MDE5MDkxM2QxYmFlZDY0NjZhNTcwNDAzYmY0Zjg1NjNhMTA1OGEyIn0%3D",
            "Referer": "https://card.tqniait.com/image/190",
            "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Linux\"",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        }
        
        params = {
            "keyword": f"{mess}",
            "image": f"{pe}"
        }
        try:
            req = requests.get(url, headers=headers, params=params).text.split("window.location = '")[1].split("'")[0]
            bot.send_photo(message.chat.id ,req,caption=" - @my00002")
        except:
            pass
    bot.reply_to(message ,"تم الانتهاء من الصنع لا تنسى الانضمام الى قناة المطور @my00002 🌺."
    
bot.infinity_polling()