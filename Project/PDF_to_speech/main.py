import pyttsx3
from PyPDF2 import PdfReader


# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    pdf_text = ""
    pdf_reader = PdfReader(pdf_file)
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()
    return pdf_text


# Function to convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()


def main():
    pdf_file = 'testdoc.pdf'

    try:
        pdf_text = extract_text_from_pdf(pdf_file)
        text_to_speech(pdf_text)
        print('Text-to-speech conversion completed.')

    except Exception as e:
        print('An error occurred:')


if __name__ == '__main__':
    main()
