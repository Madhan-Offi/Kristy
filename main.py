import telegram.ext
import os
from os import environ
import re
import base64
import requests
from urllib.parse import urlparse, parse_qs

TOKEN = environ.get('BOT_TOKEN')

def start(update, context):
    update.message.reply_text("𝗛𝗲𝘆 𝗯𝗿𝗼, 𝗜'𝗺 𝗔 𝗕𝘆𝗽𝗮𝘀𝘀𝗲𝗿 𝗜'𝗜𝗜 𝗢𝗻𝗹𝘆 𝗪𝗼𝗿𝗸 𝗙𝗼𝗿 @PrimexCloud")
    
def help(update, context):
   update.message.reply_text("""
   the following commands are available
/start -> Welcome Message

/help -> all helpful command list

/adf -> bypass adf.ly link

/droplink -> bypass droplink.co link

/gp -> bypass gplink stinky url

/rocklinks -> bypass rocklinks url

/gdtot -> GDTOT links (GDTOT CRYPT REQUIRED)

/hubdrive -> HubDrive Links (HUBDRIVE CRYPT REQUIRED)

/katdrive -> KatDrive Links (KATDRIVE CRYPT REQUIRED)

/kolop -> Kolop Links (KOLOP CRYPT REQUIRED)

/drivefire -> DriveFire Links (DRIVEFIRE CRYPT REQUIRED)

/magic -> AppDrive/DriveApp/GDFlix/DriveSharer/DriveLinks/DriveBit Links (Login required)

/generic -> use this command for these services

exe.io/exey.io
sub2unlock.net/sub2unlock.com
rekonise.com
letsboost.net
ph.apps2app.com
mboost.me
shortconnect.com
sub4unlock.com
ytsubme.com
bit.ly
social-unlock.com
boost.ink
goo.gl
shrto.ml
t.co
tinyurl.com

usage - commands{} link{https://...} (example -->/adf https://adf.ly/xyz)
   """)

def adf(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ ADFLY LINK BYPASSING ⚡️⚡️")
        os.system('python adf.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"Done")
        update.message.reply_text(f"{zkm}")
        
def generic(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ GENERIC LINK BYPASSING (UNSTABLE FAILS FREQUENTLY) ⚡️⚡️")
        os.system('python generic.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

def gp(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"𝗕𝘆𝗽𝗮𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗚𝗽𝗹𝗶𝗻𝗸 𝗟𝗶𝗻𝗸")
        os.system('python gp.py')
        update.message.reply_text(f"Done")
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

def droplink(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"𝗕𝘆𝗽𝗮𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗗𝗿𝗼𝗽𝗹𝗶𝗻𝗸 𝗟𝗶𝗻𝗸")
        os.system('python droplink.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

def gdtot(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"𝗕𝘆𝗽𝗮𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗚𝗱𝘁𝗼𝘁𝗹𝗶𝗻𝗸 𝗟𝗶𝗻𝗸")
        os.system('python gdtot.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")
        
def hubdrive(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"⚡️⚡️ HUBDRIVE LINK BYPASSING ⚡️⚡️")
        os.system('python hubdrive.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

def katdrive(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"𝗕𝘆𝗽𝗮𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗚𝗱𝘁𝗼𝘁𝗹𝗶𝗻𝗸 𝗟𝗶𝗻𝗸")
        os.system('python katdrive.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

def kolop(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"𝗕𝘆𝗽𝗮𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗚𝗱𝘁𝗼𝘁𝗹𝗶𝗻𝗸 𝗟𝗶𝗻𝗸")
        os.system('python kolop.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")
        
def drivefire(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"𝗕𝘆𝗽𝗮𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗚𝗱𝘁𝗼𝘁𝗹𝗶𝗻𝗸 𝗟𝗶𝗻𝗸")
        os.system('python drivefire.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")
        
def magic(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"𝗕𝘆𝗽𝗮𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗨𝗻𝗶𝗳𝗶𝗲𝗱 𝗟𝗶𝗻𝗸")
        os.system('python magic.py')
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

        
def rocklinks(update, context):
        zipk = context.args[0]
        open('1.txt','w').write(zipk)
        update.message.reply_text(f"𝗕𝘆𝗽𝗮𝘀𝘀𝗶𝗻𝗴 𝘆𝗼𝘂𝗿 𝗥𝗼𝗰𝗸𝗹𝗶𝗻𝗸 𝗟𝗶𝗻𝗸")
        os.system('python rocklinks.py')
        update.message.reply_text(f"Done")
        zkm = open('2.txt', 'r').read()
        update.message.reply_text(f"{zkm}")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("adf", adf))
disp.add_handler(telegram.ext.CommandHandler("droplink", droplink))
disp.add_handler(telegram.ext.CommandHandler("gdtot", gdtot))
disp.add_handler(telegram.ext.CommandHandler("hubdrive", hubdrive))
disp.add_handler(telegram.ext.CommandHandler("katdrive", katdrive))
disp.add_handler(telegram.ext.CommandHandler("kolop", kolop))
disp.add_handler(telegram.ext.CommandHandler("drivefire", drivefire))
disp.add_handler(telegram.ext.CommandHandler("magic", magic))
disp.add_handler(telegram.ext.CommandHandler("gp", gp))
disp.add_handler(telegram.ext.CommandHandler("generick", generic))
disp.add_handler(telegram.ext.CommandHandler("rocklinks", rocklinks))
updater.start_polling()
updater.idle()
