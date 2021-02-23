'''
dengan menggunakan API, akan memudahkan konfigurasi yang diperlukan.

sumber referensi: - https://pypi.org/project/RouterOS-api/
                  - https://wiki.mikrotik.com/wiki/API_command_notes#Scripting_and_API
                  - https://github.com/socialwifi/RouterOS-api
ditulis pada: 23-02-2021
'''

# untuk konfigurasinya menggunakan module routeros_api
import routeros_api

# authentikasi terlebih dahulu ke routeros dan pastikan service api sudah di enable
api = routeros_api.RouterOsApiPool('192.168.1.1', username='user1', password='user1', plaintext_login=True)

api_connect = api.get_api()

# konfigurasi router dengan membuat command
api_command = api_connect.get_resource('/ip/address')

# ambil data dari API
api_show = api_command.get()

# dan tampilkan datanya
print(api_show)