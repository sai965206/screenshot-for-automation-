import pyautogui as pg

class saving:

    def __init__(self,x,y,width,height):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def capture(self):
        self.picture = pg.screenshot(region=(self.x, self.y, self.width, self.height))
        self.picture.save("D:\\tsting\\flipkart.png")