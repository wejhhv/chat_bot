#定期的にツイッターからツイートを読み込みtxtファイルに書き込みを行っている
from requests_oauthlib import OAuth1Session,OAuth1
import json
import requests
import urllib
import MeCab
import sys
import time


#検索ワードを引数として関連するツイートを表示する関数
def twitter_search_write(word):
    #APIキーの設定
    CK="uevzqM4e45MnY28kQabaZtYLS"   #consumer_kek
    CKS="3wLtgdVy9YIinxRMlixkAgW7ccqnIqLHJrCyQdvgzdK0wlPDC6" #consumer_key_secret
    AT="1197830297489793025-LQqsFzfr9ovYoazielLfOgl5nX4zpI"  #access_token
    ATC="f3txNcNdH0Ulw7S8zqclFdJsgXDiAnYdvVgp2sPmLP0Tf" #access_token_secret

    #URLの指定　自分の情報、キーワードを投げる→twittetに送る情報
    url="https://api.twitter.com/1.1/search/tweets.json?count=100&q=" + word    #countは返す個数、keywordはキーワード
    auth= OAuth1(CK,CKS,AT,ATC)
    response=requests.get(url, auth = auth)
    change_char =dict.fromkeys(range(0x10000,sys.maxunicode + 1),0xfffd)
    #responseにtwitterからのデータが送られてくる
    data = response.json()['statuses']
    for tweet in data:
    #テキスト部分を表示
        print(tweet["text"])
        x=tweet["text"].translate(change_char)
        file=open("today.txt","a",encoding='UTF-8') #ファイルを開く、なければ作成、書き込むだけなら"w"追加するなら"a"(append),読み取るなら"r"次に言語指定
        file.write(x)
        file.close()
    

x=input("入力")
for i in range(1,10):
    
    twitter_search_write(x)
    time.sleep(5)




