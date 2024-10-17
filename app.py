import PyPDF2
from gtts import gTTS
import os


def pdf_to_text(pdf_file_path):
    """Extracts text from a PDF file."""
    try:
        with open(pdf_file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
            return text
    except FileNotFoundError:
        print(f"Error: The file {pdf_file_path} was not found.")
        return ""
    except Exception as e:
        print(f"An error occurred while reading the PDF: {e}")
        return ""


def text_to_speech(text, output_file_path):
    """Converts text to speech and saves it as an audio file."""
    try:
        if text.strip() == "":
            print("No text to convert to speech.")
            return
        tts = gTTS(text=text, lang='en')
        tts.save(output_file_path)
        print(f"Audio saved as {output_file_path}")
    except Exception as e:
        print(f"An error occurred during text-to-speech conversion: {e}")


def pdf_to_voice(pdf_file_path, output_audio_path):
    """Converts a PDF file to a voice message (audio file)."""
    text = pdf_to_text(pdf_file_path)
    if text.strip():  # Proceed if text is not empty
        text_to_speech(text, output_audio_path)
    else:
        print("No text found in the PDF or failed to extract text.")


def test_pdf_to_text():
    """Test function for PDF to text extraction."""
    pdf_file = "C:/Users/lenovo/Downloads/sample_test.pdf"  # Update with the path to your PDF
    print(f"\n--- Testing PDF to Text with file: {pdf_file} ---")
    text = pdf_to_text(pdf_file)

    if text:
        print("Extracted text from the PDF:\n")
        print(text)
    else:
        print("Failed to extract text or PDF is empty.")


def test_text_to_speech():
    """Test function for Text to Speech conversion."""
    sample_text = "This is a sample text to test the text-to-speech functionality."
    output_audio = "C:/Users/lenovo/Desktop/test_speech.mp3"  # Output audio file path
    print(f"\n--- Testing Text to Speech ---")

    text_to_speech(sample_text, output_audio)

    # Optionally play the audio file (Windows only)
    if os.path.exists(output_audio):
        print(f"Playing the audio file: {output_audio}")
        if os.name == "nt":  # For Windows systems
            os.startfile(output_audio)
    else:
        print("Audio file was not created.")


def test_pdf_to_voice():
    """Test function for PDF to Voice (PDF to Speech) conversion."""
    pdf_file = "C:/Users/lenovo/Downloads/AY9wE0ofz6.pdf"  # Update with the path to your PDF
    output_audio = "C:/Users/lenovo/Desktop/output_voice.mp3"  # Output audio file path
    print(f"\n--- Testing PDF to Voice with file: {pdf_file} ---")

    pdf_to_voice(pdf_file, output_audio)

    # Optionally play the audio file (Windows only)
    if os.path.exists(output_audio):
        print(f"Playing the audio file: {output_audio}")
        if os.name == "nt":  # For Windows systems
            os.startfile(output_audio)
    else:
        print("Audio file was not created.")


if __name__ == "__main__":
    print("Running tests for PDF to Text, Text to Speech, and PDF to Voice functions.")

    # Test PDF to Text Extraction
    # test_pdf_to_text()   # remove # for testing this

    # Test Text to Speech Conversion
    # test_text_to_speech() # remove # for testing this

    # Test PDF to Voice (Full Flow)
    test_pdf_to_voice()
