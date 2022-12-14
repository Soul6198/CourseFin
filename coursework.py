import pprint
import json
import pip._vendor.requests
from pip._vendor import requests
import time

with open('token_vk.txt', 'r') as file_object:
    token_vk = file_object.read().strip()

with open('token_ya.txt', 'r') as file_object:
    token_ya = file_object.read().strip()

vk_user_id = input('Введите id пользователя ВК: ')


class VkUser:
    def _get_photos_data(self, owner_id=vk_user_id, num=5):
        vk_url = 'https://api.vk.com/method/photos.get'
        params = {
            'access_token': token_vk,
            'owner_id': owner_id,
            'album_id': 'profile',
            'extended': 1,
            'count': num,
            'v': 5.131,
        }
        res = requests.get(url=vk_url, params=params).json()
        return res['response']['items']
        
def _get_short_data(self):
        some_data = self._get_photos_data()
        result = {}
        for i in range(len(some_data)):
            likes_count = some_data[i]['likes']['count']
            biggest_photo_url = some_data[i]['sizes'][-1]['url']
            addition_date = datetime.datetime.fromtimestamp(some_data[i]['date']).strftime("%m/%d/%Y")
            photo_size = some_data[i]['sizes'][-1]['type']
            new_value = result.get(likes_count, [])
            new_value.append({'likes_count': likes_count,
                              'addition_date': addition_date,
                              'url': biggest_photo_url,
                              'size': photo_size})
            result[likes_count] = new_value
        return result

def get_final_datas(self):
    json_for_user = []
    dict_to_send = {}
    photos_dict = self._get_short_data()
    for photo in photos_dict.keys():
         for value in photos_dict[photo]:
            if len(photos_dict[photo]) == 1:
                    file_name = f'{value["likes_count"]}.jpg'
            else:
                 file_name = f'{value["likes_count"]}_{value["addition_date"]}.jpg'
            json_for_user.append({'file name': file_name, 'size': value["size"]})
            dict_to_send[file_name] = photos_dict[photo][0]['url']
    return json_for_user, dict_to_send


class YaDisk:
    def __init__(self):
        self.token = ya_token
        self.headers = {'Authorization': self.token}

    def create_folder(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': 'Photos'}
        requests.put(url, headers=self.headers, params=params)

    def send_photos(self):
        sending_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        print('Подождите, операция выполняется')
        for key in tqdm(file_to_send.keys()):
            params = {'path': f'Photos/{key}',
                      'url': file_to_send[key],
                      'overwrite': False}
            requests.post(sending_url, headers=self.headers, params=params)
            print('Фотографии сохранены')


if __name__ == '__main__':
    yadisk = YaDisk()
    vk_user = VkUser()
    final_datas = vk_user.get_final_datas()
    file_for_user = final_datas[0]
    file_to_send = final_datas[1]
    yadisk.create_folder()
    yadisk.send_photos()
    print('json-файл с информацией по файлу:')
    pprint(file_for_user)

