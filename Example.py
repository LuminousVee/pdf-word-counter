from word_counter import count_words_in_pdf

def main():
    # Example PDF file path (replace 'sample.pdf' with your actual PDF file)
    pdf_file_path = 'sample.pdf'
    
    try:
        # Call the function to count words
        word_count = count_words_in_pdf(pdf_file_path)
        print(f"The PDF file '{pdf_file_path}' contains {word_count} words.")
    
    except FileNotFoundError:
        print(f"Error: The file '{pdf_file_path}' was not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
