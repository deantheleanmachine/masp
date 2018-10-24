import platform
import os


# def get_os():
#     os_info = platform.system()
#     if os_info == 'Darwin':
#         os_name = os.popen('sw_vers -productName').read().strip()
#         os_version = platform.mac_ver()[0]
#         os_info = f'{os_name}, v{os_version}'
#     return os_info

class OSScan():
    def __init__(self):
        self.os_info = platform.system()

    def get_details(self):
        if self.os_info == 'Darwin':
            os_name = os.popen('sw_vers -productName').read().strip()
            os_version = platform.mac_ver()[0]
            os_info = f'OS Name = {os_name}\nOS Version = v{os_version}'
        return os_info
