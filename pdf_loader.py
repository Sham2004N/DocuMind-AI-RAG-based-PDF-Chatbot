from pypdf import PdfReader #PdfReader reads pdf files page by page

def load_pdf(uploaded_files):    #creates a reusable funtion
    """
    Extract text from one or more uploaded PDF files.
    """

    text = ""

    for pdf in uploaded_files:   #Supports multiple PDF uploads.
        reader = PdfReader(pdf)  #Loads the PDF.

        for page in reader.pages: #Reads every page.
            page_text = page.extract_text() #Converts page into plain text.

            if page_text:    #Some pages contain only images. This prevents errors.
                text += page_text + "\n"

    return text 