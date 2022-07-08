from pprint import pprint
import requests

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        # pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, comp_file_patch):
        response_href = self._get_upload_link(disk_file_path=disk_file_path)
        href = response_href.get('href', '')
        response = requests.put(href, data=open(comp_file_patch, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    comp_file_patch = input('Enter the path to the file to copy (Example - /home/123.txt): ')
    token = input('Enter the token to access YandexDisk: ')
    path_list = comp_file_patch.split('/')
    file_name = path_list[-1]
    ya = YandexDisk(token=token)
    ya.upload_file_to_disk(disk_file_path=file_name, comp_file_patch=comp_file_patch)