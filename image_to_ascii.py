from PIL import Image

def asciiConvert(image, type, saveas, scale):
    # open and get image size
    img = Image.open(image)
    
    w, h = img.size

    img.resize((w//scale, h//scale)).save("resized.%s" % type)

    img = Image.open("resized.%s" % type)

