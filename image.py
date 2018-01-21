import requests
import os

class Image:
    def __init__(self,token,path = 'images'):
        if path not in os.listdir():
            os.mkdir(path)
        self.token = token
        self.path = path

    def imgpath(self,chat_id):
        return self.path + '/' + str(chat_id) + '.jpg'

    def save(self,chat_id,file_info):
        url = 'https://api.telegram.org/file/bot{0}/{1}'
        f = requests.get(url.format(self.token,file_info.file_path))
        with open(self.imgpath(chat_id),'wb') as nf:
            for ch in f:
                nf.write(ch)
