from src.utils import values_to_string
from src.pdf_service import PdfService

class IPdfService(PdfService):
    def __init__(self, file_path):
        self.file_path = "assets/" + file_path + ".pdf"
        self.__pdf_service = PdfService(key = "TEST_KEY")

    def get_pdf(self):
        return self.__pdf_service

    def get_data(self):
        try:
            data = self.get_pdf().extract(self.file_path)
            return values_to_string(data)
        except FileNotFoundError:
            raise FileNotFoundError("File not found at the specified path")
    