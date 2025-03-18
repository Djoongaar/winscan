#!/bin/python3
import os
from winreg import (
    OpenKeyEx,
    QueryInfoKey,
    HKEY_USERS,
    HKEY_LOCAL_MACHINE
)

class WinScan:

    def __init__(self):
        self.path = os.path.join(os.getcwd(), "reg")
        self.default = os.path.join(self.path, "DEFAULT")
        self.sam = os.path.join(self.path, "SAM")
        self.security = os.path.join(self.path, "SECURITY")
        self.software = os.path.join(self.path, "SOFTWARE")
        self.system_path = os.path.join(self.path, "SYSTEM")

    def get_users(self):
        with OpenKeyEx(HKEY_LOCAL_MACHINE, self.security) as user_profile:
            print(user_profile)


if __name__ == '__main__':
    winscan = WinScan()
    winscan.get_users()
