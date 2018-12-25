import requests
from bs4 import BeautifulSoup

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# root_url = 'http://www.kekenet.com/Article/15539/'
list_a = []
list_name = []


def write_text(text, name):
    save_path = "./speechdraft/" + name.replace(" ", "") + ".txt"
    text = text.replace('\n', '\r\n')
    # text = text.encode(encoding="utf-8")
    with open(save_path, 'a+') as f:  # 打开写入到path路径里-二进制文件，返回的句柄名为f
        f.write(text)  # 往f里写入r对象的二进制文件
    f.close()


def find_url(soup):
    soup = soup.find(id="menu-list").find_all('h2')
    for li in soup:
        a = li.find('a').get("href")
        name = li.find('a').get('title')
        list_a.append(a)
        list_name.append(name)


def get_text_by_url(url):
    re = requests.get(url, verify=False).content
    soup = BeautifulSoup(re, 'html5lib')
    name = soup.find("title").text[0:-12]
    text = soup.find(attrs={'class': 'info-qh'}).text
    return (name,text)
    #write_text(text, name)
    #print(name + " is ok!")


def start(root_url):
    try:
        re = requests.get(root_url, verify=False).content
        soup = BeautifulSoup(re, 'html5lib')
        find_url(soup)
        list=[]
        for i in range(0, len(list_a)):
            j = len(list_a) - i - 1
            list.append(get_text_by_url(list_a[j]))
        return list
    except:
        return None

def start_one(root_url):
    try:
        return get_text_by_url(root_url)
    except:
        return None


''' for i in range(0, len(list_a)):
     j = len(list_a) - i - 2
     if list_name[j][0:-5] == list_name[j + 1][0:-5]:
         list_name[j] = list_name[j + 1]  # 相同的文件名相同'''  # 可用但篇幅太长废除

#start_one('http://www.kekenet.com/Article/201812/572859.shtml')
#print(start('http://www.kekenet.com/Article/15539/'))
