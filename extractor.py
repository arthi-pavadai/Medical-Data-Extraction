from pdf2image import convert_from_path
from backend.src.parser_prescription import PrescriptionParser
from backend.src.parser_patient_details import Patientdetail_Parser
import pytesseract
import util

POPPLER_PATH=r'C:\Users\Artham\Release-24.08.0-0\poppler-24.08.0\Library\bin'

def extract(file_path, file_format):
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document=''
    if len(pages)>0:
        page=pages[0]
        processed_image= util.preprocess_image(page)
        text = pytesseract.pytesseract.image_to_string(processed_image, lang='eng')
        document= '\n' + text

    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document).parse()
    elif file_format == 'patient_details':
        extracted_data = Patientdetail_Parser(document).parse()
    else:
        raise Exception(f'Invalid file format: {file_format}')

    return extracted_data

#if __name__ == '__main__':
#   data= extract('../resources/prescription/pre_2.pdf','prescription')
#    data= extract('../resources/patient_details/pd_2.pdf','patient_details')
#   data= extract('../resources/patient_details/pd_2.pdf','abc')
#    print(data)