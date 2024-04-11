from PIL import Image, ImageDraw, ImageFont
from random import randint

def rand_color():
    r = randint(200, 255)
    g = randint(200, 255)
    b = randint(200, 255)
    return (r, g, b)


fin = open("vis.txt", 'r')
W, h, c = map(int, fin.readline().split())
n = int(fin.readline())
boxes = []
shift_y = 0
max_y = 0
for i in range(n):
    line = fin.readline()
    x, y, w, h, meta = line.split()
    x, y, w, h = map(int, (x, y, w, h))
    shift_y = max(shift_y, -y)
    max_y = max(max_y, y + h)
    boxes.append((x, y, w, h, meta))
H = shift_y + max_y + 1
scale = max(1, 500 / min(W, H))
W = int(W * scale)
H = int(H * scale)
im = Image.new('RGB', (W, H), (0, 0, 0))
draw = ImageDraw.Draw(im)
font_size = max(8, int(min(h, c) * scale))

# font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", font_size)
font = ImageFont.truetype("arial.ttf", font_size)

for i in range(n):
    x, y, w, h, meta = boxes[i]
    fill_col = (255, 255, 255)
    if meta == 'floating':
        fill_col = ()
        meta = '*'
    elif meta == 'embedded':
        fill_col = (220, 130, 0)
        meta = '#'
    elif meta == 'surrounded':
        fill_col = (0, 0, 127)
        meta = '$'
    else:
        fill_col = rand_color()
        meta = meta[5:]
    ny = y + shift_y

    x1 = int(x * scale)
    x2 = int((x + w) * scale)
    y1 = int(ny * scale)
    y2 = int((ny + h) * scale)
    coords = (x1, y1, x2, y2)

    if len(fill_col) == 3:
        draw.rectangle(coords, fill=fill_col, outline=rand_color())
    else:
        draw.rectangle(coords, outline=rand_color())
    text_coords = (x1, y1)
    draw.text(text_coords, meta, (127, 0, 127), font=font)
im.show()
im.save('scheme.png')
