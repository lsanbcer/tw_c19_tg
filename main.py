# encoding:utf-8
import requests
import datetime
import string

if __name__ == '__main__':

    # tg bot
    bot_token = 'your tg bot token'
    bot_chatID = 'your tg chat id'

    message_text = 'https://covid19dashboard.cdc.gov.tw/dash3'
    message_response = requests.get(message_text)

    path = './did.txt'
    f = open(path, 'r')
    text = f.read()
    f.close()

    test_message = str(datetime.date.today()) + '\n' + \
                        '確診:' + str(message_response.json()['0']['確診']) + '\n' + \
                        '死亡:' + str(message_response.json()['0']['死亡']) + ' (' + str( int((message_response.json()['0']['死亡']).replace(',', '')) - int(text) ) + ')' + '\n' + \
                        '昨日確診:' + str(message_response.json()['0']['昨日確診'])
    test_message = test_message.replace(',' , '')
    print(test_message)

    f = open(path, 'w')
    f.write(str((message_response.json()['0']['死亡']).replace(',', '')))
    f.close()
    
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + test_message

    response = requests.get(send_text)
