import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_upload_link(self, file_path: str):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        resp = requests.get(upload_url, headers=headers, params=params)
        print(resp.json())
        return resp.json()

    def upload_file_to_yadisk(self, disk_file_path, filename: str):
        href = self.get_upload_link(disk_file_path).get('href', '')
        resp = requests.put(href, data = open(filename, 'rb'))
        resp.raise_for_status()
        if resp.status_code == 201:
            print("Success")


if __name__ == '__main__':
    path_to_file = "Путь к файлу"
    path_to_file_yd = 'Путь куда сохранить на яндекс.диске'
    token = 'Токен'
    uploader = YaUploader(token)
    result = uploader.upload_file_to_yadisk(path_to_file_yd, path_to_file)