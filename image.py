from PyQt5.QtWidgets import QLabel, QFileDialog
from PyQt5.QtGui import QImage, QPixmap, QColor, qRgb
from PyQt5.QtCore import Qt

class ImageLabel(QLabel):
    """
    Класс используется для работы с лейблом изображения
    
    Основное применение - работа с изображением на экране (открытие, редактирование...).
    
    Attributes
    ----------
    image : QImage
        Изображение на экране
    original_image : QImage
        Оригинальное изображение
    parent : PhotoEditorGUI
        Окно приложения
    """
    def __init__(self, parent, image = None):
        """Конструктор класса ImageLabel"""

        super().__init__(parent)

        # parent - родительский элемент, в котором содержится QImage
        self.parent = parent 
        self.image  = QImage()

        # Вывод изображения на экран (по умолчанию - ничего)
        self.setPixmap(QPixmap().fromImage(self.image))
        self.setAlignment(Qt.AlignCenter)

    def openImage(self):
        """Функция предлагает выбрать изображение и открывает его"""

        # Открытие QFileDialog для выбора изображения нужного расширения
        image_file, _ = QFileDialog.getOpenFileName(self, "Open Image", 
                "", "PNG Files (*.png);JPG Files (*.jpeg *.jpg )")

        if image_file:

            # Сбрасываем значения
            self.parent.zoom_factor = 1
            self.brightness = 0
            self.contrast   = 0

            # TODO: здесь нужно сбросить все кнопки и слайдеры

            # Устанавливаем выбранное изображение, как свойство класса
            self.image = QImage(image_file)

            # Это копия изображения (оригинал)
            self.original_image = self.image.copy()

            # Отображение изображения на экране
            self.setPixmap(QPixmap().fromImage(self.image))
            self.resize(self.pixmap().size())

            self.parent.updateActions()

        elif image_file == '':

            # Пользватель выбрал 'Назад'
            pass
        else:

            # Какая-то другая ошибка
            pass

    def revertToOriginal(self):
        self.image = self.original_image.copy()
        self.contrast   = 0
        self.brightness = 0
        self.setPixmap(QPixmap().fromImage(self.image))
        self.repaint()

    def saveImage(self):
        # Окно выбора куда сохранять
        if self.image.isNull() == False:
            image_file, _ = QFileDialog.getSaveFileName(self, "Save Image", 
                "", "PNG Files (*.png);;JPG Files (*.jpeg *.jpg )")

            if image_file:
                self.image.save(image_file)

    def rotateImage(self, direction):
        if self.image.isNull() == False:
            if direction == "cw":
                transform90 = QTransform().rotate(90)
            elif direction == "ccw":
                transform90 = QTransform().rotate(-90)

            pixmap = QPixmap(self.image)

            rotated = pixmap.transformed(transform90, mode=Qt.SmoothTransformation)
            self.resize(self.image.height(), self.image.width())

    def convertToSepia(self):
        if self.image.isNull() == False:

            for row_pixel in range(self.image.width()):
                for col_pixel in range(self.image.height()):
                    pixel = QColor(self.image.pixel(row_pixel, col_pixel))

                    red   = pixel.red()
                    green = pixel.green()
                    blue  = pixel.blue()

                    new_red   = int(0.393 * red + 0.769 * green + 0.189 * blue)
                    new_green = int(0.349 * red + 0.686 * green + 0.168 * blue)
                    new_blue  = int(0.272 * red + 0.534 * green + 0.131 * blue)

                    red   = new_red if new_red < 256 else red
                    green = new_green if new_green < 256 else green
                    blue  = new_blue if new_blue < 256 else blue

                    new_pixel = qRgb(red, green, blue)
                    self.image.setPixel(row_pixel, col_pixel, new_pixel)

        self.setPixmap(QPixmap().fromImage(self.image))
        self.repaint()

    def convertToNegativ(self):
        if self.image.isNull() == False:
            self.image.invertPixels()
            self.setPixmap(QPixmap().fromImage(self.image))
            self.repaint()

    def convertToGray(self):
        if self.image.isNull() == False:
            grayscale_img = self.image.convertToFormat(QImage.Format_Grayscale16)
            self.image = QImage(grayscale_img)
            self.setPixmap(QPixmap().fromImage(self.image))
            self.repaint

    def changeBrighteness(self):
        brightness = self.parent.brightness_slider.value()
        print(brightness)
        for row_pixel in range(self.image.width()):
            for col_pixel in range(self.image.height()):
                pass

        self.setPixmap(QPixmap().fromImage(self.image))

    def changeContrast(self):
        contrast = self.parent.contrast_slider.value()
        print(contrast)
        for row_pixel in range(self.image.width()):
            for col_pixel in range(self.image.height()):
                pass
        
        self.setPixmap(QPixmap().fromImage(self.image))
