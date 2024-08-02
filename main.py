### Main program QHY

import cmd
import os
import time
import cv2
import numpy as np
import ctypes
from ctypes import *
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

qhyccddll = cdll.LoadLibrary('.\\Libraries\\qhyccd.dll')
# get camera id
qhyccddll.GetQHYCCDId.argtypes       =  [ctypes.c_uint32, ctypes.c_char_p]
# get handle via camera id
qhyccddll.OpenQHYCCD.argtypes        =  [ctypes.c_char_p]
qhyccddll.OpenQHYCCD.restype         =  ctypes.c_void_p
# close camera
qhyccddll.CloseQHYCCD.argtypes       =  [ctypes.c_void_p]
# initialize camera
qhyccddll.InitQHYCCD.argtypes        =  [ctypes.c_void_p]
# get camera chip information
qhyccddll.GetQHYCCDChipInfo.argtypes =  [ctypes.c_void_p,
                                         ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                         ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32),
                                         ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                         ctypes.POINTER(ctypes.c_uint32)]
# get parameters value
qhyccddll.GetQHYCCDParam.argtypes   =   [ctypes.c_void_p, ctypes.c_uint32]
qhyccddll.GetQHYCCDParam.restype    =   ctypes.c_double

class pyQHY(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to pyQHY. Type "help" for available commands.'

    def do_connect(self, line):
        print("Connecting to QHY...")

    def do_quit(self, line):
        """Exit pyQHY"""
        qhyccddll.CloseQHYCCD.argtypes = [ctypes.c_void_p]
        # self.cam.disconnect()
        # AtikSDK.ArtemisShutdown()
        return True

if __name__ == '__main__':
    # u3Handle = LJUD.openLabJack(LJUD.LJ_dtU3, LJUD.LJ_ctUSB, "1", 1)
    # LJUD.ePut(u3Handle.handle, LJUD.LJ_ioPUT_CONFIG, LJUD.LJ_chLOCALID, 0, 0)
    pyQHY().cmdloop()