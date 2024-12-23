from PIL import Image

def asciiConvert(image, type, saveas, scale):
    scale = int(scale)

    # open and get image size
    img = Image.open(image)
    w, h = img.size

    # resize image (downscale)
    img.resize((w // scale, h // scale)).save("resized.%s" % type)

    # open new image
    img = Image.open("resized.%s" % type)
    w, h = img.size  # get new width and height 

    # list with correct length and height (same as resized image)
    grid = []
    for i in range(h):
        grid.append([])  # Make each row an empty list

    pix = img.load()

    for y in range(h):
        for x in range(w):
            if sum(pix[x, y]) == 0:
                grid[y].append("#")
            elif sum(pix[x, y]) in range(1, 100):
                grid[y].append("X")
            elif sum(pix[x, y]) in range(100, 200):
                grid[y].append("%")
            elif sum(pix[x, y]) in range(200, 300):
                grid[y].append("&")
            elif sum(pix[x, y]) in range(300, 400):
                grid[y].append("*")
            elif sum(pix[x, y]) in range(400, 500):
                grid[y].append("+")
            elif sum(pix[x, y]) in range(500, 600):
                grid[y].append("/")
            elif sum(pix[x, y]) in range(600, 700):
                grid[y].append("(")
            elif sum(pix[x, y]) in range(700, 750):
                grid[y].append("'")
            else:
                grid[y].append(" ")

    # create the ascii art and save it
    art = open(saveas, "w")

    for row in grid:
        art.write(" ".join(row) + "\n")  # add a space between characters in each row

    art.close()

if __name__ == '__main__':
    asciiConvert("SnorlaxChilling.jpg", "jpg", "SnorlaxChilling.txt", "10")

#resource used
#https://www.geeksforgeeks.org/working-images-python/