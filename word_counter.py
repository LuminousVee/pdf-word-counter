import pdfplumber

def count_words_in_pdf(pdf_path):
    """
    Count the number of words in a given PDF file.

    Args:
        pdf_path (str): The path to the PDF file.

    Returns:
        int: The total number of words in the PDF.
    """
    # Initialize word count
    total_words = 0
    
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        # Loop through each page in the PDF
        for page in pdf.pages:
            # Extract text from the page
            text = page.extract_text()
            
            # Make sure there's text on the page
            if text:
                # Split the text into words and count them
                words = text.split()
                total_words += len(words)

    return total_words


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python word_counter.py <pdf_path>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    try:
        word_count = count_words_in_pdf(pdf_path)
        print(f"Total number of words in the PDF: {word_count}")
    except FileNotFoundError:
        print(f"Error: File '{pdf_path}' not found.")
