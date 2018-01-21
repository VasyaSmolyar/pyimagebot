from PIL import Image,ImageDraw

class Writer:
    def __init__(self,img_name):
        self.name = 'images/{}_tmp.jpg'.format(img_name)
        self.img = Image.open('images/{}.jpg'.format(img_name))
        self.size = self.img.size
        self.draw = ImageDraw.Draw(self.img)

    def gray(self):
        pix = self.img.load()
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                a, b, c = pix[i ,j]
                S = (a + b + c) // 3
                self.draw.point((i,j),(S,S,S))
        self.img.save(open(self.name,'wb'))

    def sepia(self,depth=30):
        pix = self.img.load()
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                a, b, c = pix[i ,j]
                S = (a + b + c) // 3
                a = S + depth * 2
                b = S + depth
                c = S
                if a > 255:
                    a = 255
                if b > 255:
                    b = 255
                if c > 255:
                    c = 255
                self.draw.point((i,j),(a,b,c))
        self.img.save(open(self.name,'wb'))

    def negate(self):
        pix = self.img.load()
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                a, b, c = pix[i ,j]
                self.draw.point((i,j),(255 - a,255 - b,255 - c))
        self.img.save(open(self.name,'wb'))
