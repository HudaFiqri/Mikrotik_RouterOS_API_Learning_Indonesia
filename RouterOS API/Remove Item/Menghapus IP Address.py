'''
dengan menggunakan API, akan memudahkan konfigurasi yang diperlukan.

sumber referensi: - https://pypi.org/project/RouterOS-api/
                  - https://wiki.mikrotik.com/wiki/API_command_notes#Scripting_and_API
                  - https://github.com/socialwifi/RouterOS-api
ditulis pada: 23-02-2021
'''

# import module yang akan digunakan
import routeros_api

# authentikasi ke router mikrotik
api = routeros_api.RouterOsApiPool('192.168.1.1', username='user1', password='user1', plaintext_login=True)
api_connect = api.get_api()

# set API ke ip address
api_command = api_connect.get_resource('/ip/address')

'''
-> hapus ip address dengan menggunakan number
sama halnya dengan command line pada mikrotik '/ip address remove numbers=1'
tapi yang untuk digunakan pada variabel panggilannya adalah variabel yang berasal dari command line.
'''
api_command.remove(numbers='1')