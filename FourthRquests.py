import requests
import json


if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }
    response = requests.get(url=url, params=param, headers=headers)

    List_data = response.json()

    fp = open('./douban1.json', 'w', encoding='utf-8')
    json.dump(List_data, fp=fp, ensure_ascii=False)

    print('work done!!')

