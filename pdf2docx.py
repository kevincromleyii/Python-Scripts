from pdf2docx import Converter

def convert_pdf_to_docx(pdf_file, docx_file):
    # Create a converter object
    converter = Converter(pdf_file)

    # Convert the PDF to DOCX
    converter.convert(docx_file, start=0, end=None)

    # Close the converter
    converter.close()

# Specify the input PDF file path
pdf_file = 'C:\\Users\\mcrom\\OneDrive\\Desktop\\Black Modern Professional Resume.pdf'

# Specify the output DOCX file path
docx_file = 'C:\\Users\\mcrom\\OneDrive\\Desktop\\Black Modern Professional Resume.docx'

# Call the function to convert the PDF to DOCX
convert_pdf_to_docx(pdf_file, docx_file)