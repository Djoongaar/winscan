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
        print(os.listdir(self.path))
        with OpenKeyEx(HKEY_LOCAL_MACHINE, self.default) as user_profile:
            for i in range(QueryInfoKey(user_profile)[0]):
                print(i)


if __name__ == '__main__':
    winscan = WinScan()
    print(winscan.default)
    winscan.get_users()
