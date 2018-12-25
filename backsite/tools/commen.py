import os
from backsite.settings import MEDIA_ROOT
from backsite.settings import MEDIA_URL
# 文件内容，文件名，保存文件夹名称
import random
from datetime import datetime

def write_text(text, name, dirct):
    name = name[10:].replace(" ", "") + ".txt"
    path = os.path.join(MEDIA_ROOT, dirct, name)
    text = text.replace('\n', '\r\n')
    text = text.encode(encoding="utf-8")
    with open(path, 'wb') as f:  # 打开写入到path路径里-二进制文件，返回的句柄名为f
        f.write(text)  # 往f里写入r对象的二进制文件
    f.close()
    return (name, text, MEDIA_URL + dirct + name)

def getRandomName():
    return datetime.now().strftime(r"%Y%m%d%H%M%S")+str(random.randrange(0, 100))
