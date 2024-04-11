# для работы функции match необходим python >= 3.10
from __future__ import annotations

from bisect import insort_left
from collections import deque
from dataclasses import dataclass
from enum import IntEnum


class ImageType(IntEnum):
    """
    Класс типа изображения
    """
    EMBEDDED = 0
    SURROUNDED = 1
    FLOATING = 2


@dataclass
class Image:
    """
    Класс изображения
    """
    width: int  # ширина
    height: int  # высота
    dx: int  # смещение по x
    dy: int  # смещение по y
    type: ImageType  # тип изображения


class Fragment:
    """
    Класс фрагмента строки
    """
    def __init__(self, width: int, dx: int):
        self.remain_width: int = width  # свободная ширина фрагмента
        self.width: int = width  # ширина фрагмента
        self.dx: int = dx  # координата х верхней границы фрагмента
        self.is_first = True  # флаг первого фрагмента
        self.right_corner_x: int = dx  # x по правому углу, концу фрагмента
        self.right_corner_y: int = 0  # y по правому углу, концу фрагмента

    def checkCapacity(self, token_width: int, is_surrounded: int) -> bool:
        """
        Функция проверки вместимости объекта в фрагмент строки
        :param token_width: ширина объекта
        :param is_surrounded: обтекаемость объекта
        :return: True - вмещает token_width фрагмент, False - не вмещает token_width
        """
        if self.is_first or is_surrounded:
            return token_width <= self.remain_width
        return token_width + char_w <= self.remain_width

    def addWord(self, token_width: int):
        """
        Функция добавления слова в фрагмент
        :param token_width: ширина слова
        :return: смещает указатели во фрагменте по длине слова
        """
        if self.is_first:
            self.remain_width -= token_width
            self.is_first = False
        else:
            self.remain_width -= token_width + char_w
        self.right_corner_x = self.dx + self.width - self.remain_width
        self.right_corner_y = 0

    def addEmbeddedImage(self, image: Image):
        """
        Функция добавления Embedded картинки в фрагмент
        :param image: вставляемая картинка
        :return: смещает указатели во фрагменте по длине картинки
        """
        if self.is_first:
            image.dx = self.dx + self.width - self.remain_width  # координата верхней границы картинки по х
            self.remain_width -= image.width
            self.is_first = False
        else:
            image.dx = self.dx + self.width - self.remain_width + char_w
            self.remain_width -= image.width + char_w
        self.right_corner_x = self.dx + self.width - self.remain_width
        self.right_corner_y = 0

    def addSurroundedImage(self, image: Image):
        """
        Функция добавления Surrounded картинки в фрагмент
        :param image: вставляемая картинка
        :return: смещает указатели во фрагменте по длине картинки
        """
        image.dx = self.dx + self.width - self.remain_width  # координата верхней границы картинки по х
        self.remain_width -= image.width
        self.is_first = True
        self.right_corner_x = self.dx + self.width - self.remain_width
        self.right_corner_y = 0

    def addFloatingImage(self, image: Image, absolute_dy: int):
        """
        Функция добавления Floating картинки в фрагмент
        :param image: вставляемая картинка
        :param absolute_dy: смещение по y для изображений floating
        :return: смещает указатели во фрагменте по длине картинки
        """
        if self.right_corner_x + image.dx >= 0:
            if self.right_corner_x + image.dx + image.width <= file_width:
                image.dx = self.right_corner_x + image.dx  # координата верхней границы картинки по х
            else:
                shift: int = self.right_corner_x + image.dx + image.width - file_width  # сдвиг картинки по х, при заходе за границу листа
                image.dx = self.right_corner_x + image.dx - shift
        else:
            image.dx = 0

        self.right_corner_x = image.dx + image.width
        self.right_corner_y = image.dy + self.right_corner_y
        image.dy = absolute_dy + self.right_corner_y  # координата верхней границы картинки по y


class FileString:
    """
    Класс строки файла
    """
    def __init__(self, images: list[Image]):
        self.height: int = file_height  # высота строки
        self.fragments: deque[Fragment] = deque()  # массив фрагментов строки
        self.createFragments(images)  # разделение строки на фрагменты по картинкам

    def createFragments(self, images: list[Image]):
        """
        Функция разбиения строки на фрагменты
        :param images: список картинок в строке
        :return: изменяет список фрагментов строки
        """
        if images:
            if images[0].dx != 0:
                self.fragments.append(Fragment(images[0].dx, 0))
            for i in range(len(images) - 1):
                new_width: int = images[i + 1].dx - images[i].dx - images[i].width  # новая ширина фрагмента, для фрагментов больше images[i].width
                if new_width != 0:
                    self.fragments.append(Fragment(new_width, images[i].dx + images[i].width))

            right_corner: int = images[-1].dx + images[-1].width  # правый угол фрагмента, конец фрагмента
            if right_corner != file_width:
                self.fragments.append(Fragment(file_width - right_corner, right_corner))
        else:
            self.fragments.append(Fragment(file_width, 0))

    def addWord(self, width) -> bool:
        """
        Фукнция добавления слова в строку
        :param width: ширина слова
        :return: добавляет слово в найденный свободный фрагмент строки
        """
        while self.fragments:
            cur_fragment: Fragment = self.fragments[0]  # текущий фрагмент
            if cur_fragment.checkCapacity(width, False):
                cur_fragment.addWord(width)
                return True
            self.fragments.popleft()

        return False

    def addEmbeddedImage(self, image: Image):
        """
        Функция добавления Embedded картинки в строку
        :param image: картинка
        :return: добавляет картинку в найденный свободный фрагмент строки
        """
        while self.fragments:
            cur_fragment: Fragment = self.fragments[0]
            if cur_fragment.checkCapacity(image.width, False):  # текущий фрагмент
                cur_fragment.addEmbeddedImage(image)
                self.height = max(self.height, image.height)
                return True
            self.fragments.popleft()

        return False

    def addSurroundedImage(self, image: Image):
        """
        Функция добавления Surrounded картинки в строку
        :param image: картинка
        :return: добавляет картинку в найденный свободный фрагмент строки
        """
        while self.fragments:
            cur_fragment: Fragment = self.fragments[0]  # текущий фрагмент
            if cur_fragment.checkCapacity(image.width, True):
                cur_fragment.addSurroundedImage(image)
                return True
            self.fragments.popleft()

        return False

    def addFloatingImage(self, image: Image, absolute_dy: int):
        """
        Функция добавления Floating картинки в строку
        :param image: картинка
        :param absolute_dy: значение y для floating картинки
        :return: добавляет картинку в первый фрагмент
        """
        self.fragments[0].addFloatingImage(image, absolute_dy)


class Paragraph:
    """
    Класс параграфа файла
    """
    def __init__(self, dy: int):
        self.height: int = 0  # высота параграфа
        self.dy: int = dy  # y координата верхней границы параграфа
        self.images: list[Image] = []  # список отслеживаемых изображений
        self.strings: list[FileString] = [FileString(self.images)]  # список строк

    def addString(self):
        """
        Функция добавления строки в параграф
        :return: увеличивает height параграфа, изменяет список строк параграфа
        """
        self.height += self.strings[-1].height
        self.refreshImages()
        self.strings.append(FileString(self.images))

    def refreshImages(self):
        """
        Функция обновления списка отслеживаемых изображений
        :return: убирает из списка вписанные в параграф изображения
        """
        new_images: list[Image] = []
        for image in self.images:
            if self.dy + self.height < image.dy + image.height:
                new_images.append(image)
        self.images = new_images

    def addWord(self, width):
        """
        Функция добавления слова в параграф
        :param width: ширина слова
        :return: добавляет слово в параграф
        """
        while not self.strings[-1].addWord(width):
            self.addString()

    def addImage(self, image: Image):
        """
        Функция добавления картинки в параграф
        :param image: картинка
        :return: добавляет картинку в параграф
        """
        match image.type:
            case ImageType.EMBEDDED:
                while not self.strings[-1].addEmbeddedImage(image):
                    self.addString()
                image.dy = self.dy + self.height  # координата y верхней границы картинки

            case ImageType.SURROUNDED:
                while not self.strings[-1].addSurroundedImage(image):
                    self.addString()
                image.dy = self.dy + self.height
                insort_left(self.images, image, key=lambda elem: elem.dx)

            case ImageType.FLOATING:
                self.strings[-1].addFloatingImage(image, self.dy + self.height)
        # выводим в ответ координаты x, y правого левого угла картинки в документе
        print(image.dx, image.dy)

    def endParagraph(self):
        """
        Функция окончания параграфа
        :return: пересчитывает высоту параграфа
        """
        self.addString()
        if self.images:
            max_h: Image = max(self.images, key=lambda elem: elem.dy + elem.height)
            diff: int = max_h.dy + max_h.height - self.height
            if diff > 0:
                self.height += diff


class File:
    """
    Класс документа
    """
    def __init__(self):
        self.height: int = 0  # высота
        self.paragraphs: list[Paragraph] = [Paragraph(0)]  # список параграфов

    def parseString(self, string: str):
        """
        Функция получения данных из входящего файла
        :param string: строка данных
        :return: добавляет в создаваемый документ слова и строки из строки данных
        """
        token_w: int = 0  # ширина добавляемого слова
        is_empty: bool = True  # флаг разделителя
        i: int = 0  # индекс символа в string
        while i < len(string):  # проходим по символам строки
            if string[i] not in " \t\n":  # если символ не разделение
                is_empty = False  # убираем флаг разделителя
                if string[i] != "(":  # если не начало картинки, увеличиваем ширину слова
                    token_w += char_w
                    i += 1
                else:  # иначе находим конец картинки, получаем ее данные, добавляем в документ
                    new_i = string.find(")", i + 1)
                    image = self.parseString2Image(string, i + 1, new_i)
                    self.paragraphs[-1].addImage(image)
                    i = new_i + 1

            else:  # если символ - разделитель
                if token_w != 0:  # если есть слово - добавляем слово в документ
                    self.paragraphs[-1].addWord(token_w)
                    token_w = 0
                i += 1

        if token_w != 0:  # добавляем последнее слово в документ
            self.paragraphs[-1].addWord(token_w)

        if is_empty:  # если пустая строка - заканчиваем параграф
            self.paragraphs[-1].endParagraph()
            self.height += self.paragraphs[-1].height
            self.paragraphs.append(Paragraph(self.height))

    def parseString2Image(self, string: str, start: int, end: int) -> Image:
        """
        Функция получения данных о картинке
        :param string: строка данных
        :param start: начало блока описания картинки
        :param end: конец блока описания картинки
        :return: Image c параметрами (ширина, высота, смещение по x, смещение по y, тип картинки)
        """
        image_arr: list[str] = string[start:end].split()[1:]  # блок описания картинки

        key_val = [elem.split('=') for elem in image_arr]  # параметры картинки ключ-значение
        dx = dy = 0  # исходные смещения картинки
        for key, val in key_val:  # проходим по параметрам картинки
            match key:  # сравниваем ключ
                case 'layout':  # для значения layout сохранияем тип картинки из ImageType
                    if val == 'embedded':
                        image_type = ImageType.EMBEDDED
                    elif val == 'surrounded':
                        image_type = ImageType.SURROUNDED
                    else:
                        image_type = ImageType.FLOATING
                case 'width':  # для значения width сохранияем ширину картинки
                    width = int(val)
                case 'height':  # для значения height сохранияем высоту картинки
                    height = int(val)
                case 'dx':  # для значения dx сохранияем смещение x картинки
                    dx = int(val)
                case 'dy':  # для значения dy сохранияем смещение y картинки
                    dy = int(val)

        return Image(width, height, dx, dy, image_type)

# считываем данные
with open('input.txt', 'r') as fin:
    file_width, file_height, char_w = map(int, fin.readline().split())  # ширина страницы, высота строки, ширина символа
    file: File = File()  # переменная документа
    lines: list[str] = []  # массив конечных строк, без разбиения

    cur_line: str = ""  # текущая строка
    for line in fin:  # проходим по строкам в входящем файле
        if not line.rstrip():  # если строка не разбита
            lines.append(cur_line)  # добавляем cur_line к строкам
            lines.append("")  # добавляем разделитель
            cur_line = ""
        else:  # иначе, добавляем к текущей строке продолжение
            cur_line += " " + line.rstrip()
    lines.append(cur_line)  # добавляем cur_line к строкам

    for line in lines:  # проходим строкам в lines
        file.parseString(line)  # переносим строку в file