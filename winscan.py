#!/bin/python3
import os
import winreg

class WinScan:

    def __init__(self, path="reg"):
        self.default = os.path.join(path, "DEFAULT")
        self.sam = os.path.join(path, "SAM")
        self.security = os.path.join(path, "SECURITY")
        self.software = os.path.join(path, "SOFTWARE")
        self.system_path = os.path.join(path, "SYSTEM")


if __name__ == '__main__':
    winscan = WinScan()
    print(winscan.system_path)
