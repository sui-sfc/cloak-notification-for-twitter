from bs4 import BeautifulSoup
import requests
import time

#cloakのn番目のチケットを取得
def get_cloak_ticket_info(url,n):
    n = str(n)
    while(1):
        try:  
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")
            
            #if system maintenance error
            '''
            if 'error_block' in soup.select('#wrapper > div > div > div')[0].get('class'):
                print('system maintenance')
                time.sleep(3600)
            '''
            performance_name = soup.select(
                '#wrapper > div > div.item_result_wrapper > ol:nth-child(' + n+ 
                ') > div > a > h1'
            )[0].contents[0]

            performance_date = soup.select(
                '#wrapper > div > div.item_result_wrapper > ol:nth-child('+ n +
                ') > div > a > div.item_header.clearfix > div > p:nth-child(1)'
            )[0].contents[0]

            sheets = soup.select(
                '#wrapper > div > div.item_result_wrapper > ol:nth-child('+ n +
                ') > div > a > div.item_result_box_msg > span > span:nth-child(1)'
            )[0].contents[0]

            ticket = soup.select(
                '#wrapper > div > div.item_result_wrapper > ol:nth-child('+ n +
                ') > div > a > div.item_result_box_msg > p'
            )[0].contents[0]
            
            price = soup.select(
                '#wrapper > div > div.item_result_wrapper > ol:nth-child(' + n +
                ') > div > a > div.item_total > span:nth-child(2)'
            )[0].contents[0]
            '''
            buy_url = soup.select(
                '#wrapper > div > div.item_result_wrapper > ol:nth-child(' + n +
                ') > div > a'
            )
            '''
            #チケットURL
            buy_url = soup.find_all('a')
            tmp = []
            for i in buy_url:
                if 'item/detail' in i.get('href'):
                    tmp.append(i.get('href'))
            buy_url = 'https://cloak.pia.jp' + tmp[int(n)-1]
            break
        except IndexError:
            print('continue')
            time.sleep(5)
            continue
    ticket_info = {'name': str(performance_name.replace('\u3000', '')), 'date': str(performance_date), 'ticket': str(
        ticket), 'sheets': str(sheets), 'price': str(price), 'url': str(buy_url)}

    return ticket_info
