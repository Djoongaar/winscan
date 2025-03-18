#!/bin/python3
import os
from winreg import (
    OpenKeyEx,
    QueryInfoKey,
    HKEY_USERS,
    HKEY_LOCAL_MACHINE
)

class WinScan:

    def __init__(self, path="reg"):
        self.default = os.path.join(path, "DEFAULT")
        self.sam = os.path.join(path, "SAM")
        self.security = os.path.join(path, "SECURITY")
        self.software = os.path.join(path, "SOFTWARE")
        self.system_path = os.path.join(path, "SYSTEM")

    def get_users(self):
        with OpenKeyEx(HKEY_LOCAL_MACHINE, self.system_path) as user_profile:
            for i in range(QueryInfoKey(user_profile)[0]):
                print(i)


if __name__ == '__main__':
    winscan = WinScan()
    print(winscan.system_path)
    winscan.get_users()
