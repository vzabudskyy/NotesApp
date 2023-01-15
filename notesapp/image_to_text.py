import cv2
import pytesseract
from numpy import asarray


PATH_TO_TESSERACT = r'C:\Users\Vladislav\AppData\Local\Tesseract-OCR\tesseract.exe'


class ImgToTxtConverter:
    def __init__(self, tsrt):
        self.__tsrt = tsrt
        pytesseract.pytesseract.tesseract_cmd = tsrt

    # converting image to grayscale
    @staticmethod
    def __to_grayscale(image: bytearray):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # binarize image grayscaled image
    @staticmethod
    def __binarization(grayscale_im):
        ret, thresh = cv2.threshold(grayscale_im, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        return thresh

    # converting binarized image to text
    @staticmethod
    def __to_text(binarized_image):
        return pytesseract.image_to_string(binarized_image)

    # run method
    def run(self, file):
        image = asarray(bytearray(file))
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        image = self.__to_grayscale(image)
        t_image = self.__binarization(image)

        return pytesseract.image_to_string(t_image)


if __name__ == "__main__":
    path_to_image = 'C:\\Users\\Vladislav\\Desktop\\django notes design\\print_sample_1.jpg'
    #converter = ImgToTxtConverter(PATH_TO_TESSERACT)
