"""
The purpose of this project is to obtain a video lecture from 
the platfom Canvas

"""

import requests
from bs4 import BeautifulSoup

url = 'https://tilburguniversity.instructure.com/courses/8907/modules/items/325669'


def get_link():

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.findAll('a')

    videos_links = [url + link['href'] for link in links if link['href'].endswith('mp4')]

    return videos_links


def download_series(links):

    for link in links:
        file_name = link.split('/')[-1]
        print('Downloading file:%s' % file_name)

        r = requests.get(link, stream=True)

        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                if chunk:
                    f.write(chunk)

        print("%s downloaded\n" % file_name)

    print('All videos downloaded!')
    return 1


if __name__ == '__main__':
    video_links = get_link()
    download_series(video_links)
