import PyPDF2 # type: ignore
import dictionary

def read_pdf(file_path):
    """
    Reads text from a PDF file.

    Args:
    file_path (str): The path to the PDF file.

    Returns:
    str: The text extracted from the PDF.
    """
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        text = ''
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
        return text

def save_to_pdf(text, output_file_path):
    """
    Saves text to a PDF file.

    Args:
    text (str): The text to be saved.
    output_file_path (str): The path to save the PDF file.

    Returns:
    None
    """
    with open(output_file_path, 'w') as file:
        file.write(text)

def main():
    # Path to the PDF file
    pdf_file_path = "pvsnp.pdf"
    
    # Read the PDF file and extract all text
    pdf_text = read_pdf(pdf_file_path)
    
    # Load the dictionary data
    dictionary_file_path = "dictionary.json"
    dictionary_data = dictionary.load_dictionary(dictionary_file_path)
    
    # Provide definitions for the extracted text using the loaded dictionary data
    print("Providing definitions for text from PDF...")
    definitions_text = dictionary.provide_definitions(pdf_text, dictionary_data)
    
    # Save the definitions as a PDF file
    output_pdf_path = "pvsnp_definitions_output.pdf"
    save_to_pdf(definitions_text, output_pdf_path)
    print("Definitions saved to:", output_pdf_path)

if __name__ == "__main__":
    main()
