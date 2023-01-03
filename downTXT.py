import urllib.request
import ixml
import ssl
from urllib import request, error
def download(): #txt小说爬虫
    i = 26
    while 1:
        page = str(i)
        pic_url = f"https://www.feiku6.com/read/s3-xueyuhuotangelianwangchaoshi/{page}.html"
        filename = f'./book/{page}.txt'
        urllib.request.urlretrieve(pic_url,filename)
        print(f"Downloading page {page}...")
        i += 1

if __name__ == '__main__':
    #ssl._create_default_https_context = ssl.create_default_context()
    #re = urllib.request.urlopen("https://s3.ananas.chaoxing.com/doc/9a/e9/f9/a50e7fed8886ec89cb44bdf268b510aa/thumb/1.png")
    try:
        download()
    except error.HTTPError as e:
        print('HTTPError 异常')
        print('reason:'+ str(e.reason), 'code:'+str(e.code), 'headers:'+str(e.headers),sep='\n')
    except error.URLError as e:
        print('URLError 异常')
        print('reason:'+ str(e.reason))
