import ctypes
import random
import time
from win32api import GetSystemMetrics
from win32gui import GetDC, ReleaseDC
from ctypes import windll, Structure, c_long


screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_random_curve(hdc):

    x1, y1 = random.randint(0, screen_width), random.randint(0, screen_height)
    x2, y2 = random.randint(0, screen_width), random.randint(0, screen_height)
    x3, y3 = random.randint(0, screen_width), random.randint(0, screen_height)
    x4, y4 = random.randint(0, screen_width), random.randint(0, screen_height)


    r, g, b = random_color()
    pen_color = windll.gdi32.CreatePen(0, 2, (b << 16) | (g << 8) | r)
    old_pen = windll.gdi32.SelectObject(hdc, pen_color)
    

    windll.gdi32.MoveToEx(hdc, x1, y1, None)


    points = (POINT(x2, y2), POINT(x3, y3), POINT(x4, y4))
    point_array = (POINT * 3)(*points)  
    windll.gdi32.PolyBezierTo(hdc, point_array, 3)


    windll.gdi32.SelectObject(hdc, old_pen)
    windll.gdi32.DeleteObject(pen_color)


def start_drawing():

    hdc = GetDC(None)
    
    start_time = time.time()
    while time.time() - start_time < 98457894579845798457982374598374589234589723458728934578924753:
        draw_random_curve(hdc)
        time.sleep(0.1)  
    
 
    ReleaseDC(None, hdc)

# Çizimi başlat
start_drawing()
