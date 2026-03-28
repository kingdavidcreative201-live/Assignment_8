from graphics import GraphWin, Image as GraphicsImage, Point, color_rgb
import os

class Image:
    def __init__(self, width_or_filename, height=None):
        if isinstance(width_or_filename, str):
            base_path = os.path.dirname(os.path.abspath(__file__))
            self.filename = os.path.join(base_path, width_or_filename)
            self.image = GraphicsImage(Point(0, 0), self.filename)
        else:
            self.image = GraphicsImage(Point(0, 0), width_or_filename, height)
    
    def getWidth(self):
        return self.image.getWidth()

    def getHeight(self):
        return self.image.getHeight()

    def getPixel(self, x, y):
        return tuple(self.image.getPixel(x, y))

    def setPixel(self, x, y, color):
        self.image.setPixel(x, y, color_rgb(*color))
    
    def draw(self):
        width, height = self.getWidth(), self.getHeight()
        win = GraphWin("Image Viewer", width, height)
        self.image.move(width // 2, height // 2)
        self.image.draw(win)
        win.getMouse() 
        win.close()

    def save(self, filename=""):
        if filename == "": filename = self.filename
        self.image.save(filename)

    def clone(self):
        cloned_image = self.image.clone()
        new_obj = Image.__new__(Image)
        new_obj.image = cloned_image
        return new_obj