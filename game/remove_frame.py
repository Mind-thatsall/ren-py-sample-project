import sys
import os

if sys.platform.startswith('win'):
    import ctypes
    import ctypes.wintypes

    # Define the necessary WinAPI constants and functions
    GWL_STYLE = -16
    WS_POPUP = 0x80000000
    SWP_FRAMECHANGED = 0x0020

    SetWindowLongW = ctypes.windll.user32.SetWindowLongW
    SetWindowPos = ctypes.windll.user32.SetWindowPos
    GetWindowLongW = ctypes.windll.user32.GetWindowLongW

    def remove_window_frame():
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        style = GetWindowLongW(hwnd, GWL_STYLE)
        style = style & ~WS_POPUP
        SetWindowLongW(hwnd, GWL_STYLE, style)
        SetWindowPos(hwnd, 0, 0, 0, 0, 0, SWP_FRAMECHANGED)

elif sys.platform.startswith('darwin'):
    def remove_window_frame():
        # Not supported on macOS
        pass

elif sys.platform.startswith('linux'):
    def remove_window_frame():
        # Not supported on Linux
        pass

else:
    def remove_window_frame():
        # Unsupported platform
        pass

remove_window_frame()
