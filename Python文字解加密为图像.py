'''
python 3.10
2022/07/25
Pycharm
'''
import math

from PIL import Image


def encode(text):
    str_len = len(text)
    width = math.ceil(str_len ** 0.5)
    img = Image.new("RGB", (width, width), 0x0)

    x, y = 0, 0
    for i in text:
        index = ord(i)
        rgb = (0, (index & 0xFF00) >> 8, index & 0xFF)
        img.putpixel((x, y), rgb)
        if x == width - 1:
            x = 0
            y += 1
        else:
            x += 1
    return img


def decode(img):
    width, height = img.size
    list = []
    for y in range(height):
        for x in range(width):
            red, green, blue = img.getpixel((x, y))
            if (blue | green | red) == 0:
                break
            index = (green << 8) + blue
            list.append(chr(index))
    return ''.join(list)


if __nae__ == '__main__':
    with open('三国演义.txt', encoding="utf-8") as file:
        all_text = file.read()
    img = encode(all_text)
    img.save("out.bmp")
    # 解码的主函数
    # all_text = decode(Image.open("out.bmp", "r"))
    # with open("decode.txt", "w", encoding="utf-8") as file:
    #     file.write(all_text)
