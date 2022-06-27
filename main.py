import json
import time
import get_info
import tweepy
import tokens
import discord
from discord.ext import tasks
import asyncio

#ファイル保存
def f_write(ticket_info):
    tf = open("latest_ticket.json", "w")
    json.dump(ticket_info, tf)
    tf.close()

#ファイル読み出し
def f_read():
    tf = open("latest_ticket.json", "r")
    latest_data = json.load(tf)
    tf.close()
    return latest_data

#メッセージ作成
def s_message(ticket_info):
    tmp = []
    for i in ticket_info.keys():
        tmp.append(ticket_info.get(i))
        message = '\n'.join(tmp)
    return message

    
url = tokens.url()



client = tweepy.Client(
    consumer_key=tokens.KEY(),
    consumer_secret=tokens.KEY_SECRET(),
    access_token=tokens.A_TOKEN(),
    access_token_secret=tokens.A_TOKEN_SECRET()
)



#チケット情報送信
def SendMessage(ticket_info):
    client.create_tweet(text=s_message(ticket_info))
    f_write(ticket_info)
    print('posted')
#ログイン

def on_ready():
    print('boot')
    #ファイルの存在確認
    #jsonが存在した時
    try:
        latast_data = f_read()
        ticket_info = get_info.get_cloak_ticket_info(url, 1)
        if latast_data == ticket_info:
            pass
        else:
            SendMessage(ticket_info)
    #存在しなかった時
    except FileNotFoundError:
        print('初回起動')
        ticket_info = get_info.get_cloak_ticket_info(url, 1)
        SendMessage(ticket_info)
        f_write(ticket_info)    #共にする処理
    print('run')
    while(1):
        timeloop()

  
#無限ループ
def timeloop():
    print('loop')
    try:
        latast_data = f_read()
        ticket_info = get_info.get_cloak_ticket_info(url, 1)
        if latast_data == ticket_info:
            pass
        else:
            SendMessage(ticket_info)
            print('posted')
    except:
        pass
    time.sleep(30)
    
    
on_ready()
