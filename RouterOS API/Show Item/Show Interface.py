'''
menampilkan interface menggunakan API.

sumber referensi: - https://pypi.org/project/RouterOS-api/
                  - https://wiki.mikrotik.com/wiki/API_command_notes#Scripting_and_API
                  - https://github.com/socialwifi/RouterOS-api
ditulis pada: 23-02-2021
'''

# import module yang diperlukan
import routeros_api

# authentikasi ke router mikrotik
api = routeros_api.RouterOsApiPool('192.168.1.1', username='user1', password='user1', plaintext_login=True)
api_connect = api.get_api()

# set API ke interface
api_command = api_connect.get_resource('/interface')

# ambil data dari api
api_show = api_command.get()

# dan tampilkan datanya
print(api_show)