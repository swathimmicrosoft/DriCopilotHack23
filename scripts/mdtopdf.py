# This code example demonstrates how to convert a Markdoen file to a PDF document.
import markdown
import os
import pdfkit 
from pdfkit import from_file

# Defining main function
def main():
    # The location where the markdown files are located
    input_path = "C:\\Users\\swathim\\Downloads\\documentation\\documentation\\content"

    # The location where we will write the PDF files
    output_path = "C:\\Users\\swathim\\Desktop\\hackathon23Github\\DriCopilotHack23\\DriCopilotHack23\\data"

    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

    # list to store files name
    res = []
    for (dir_path, dir_names, file_names) in os.walk(input_path):
        for file_name in file_names:
            if file_name.endswith('.md'):

                try:
                            # Construct the input and output file paths
                            input_file_path = os.path.join(dir_path, file_name)
                            output_file_path = os.path.join(output_path, file_name.replace('.md', '.pdf'))

                            # Convert the markdown file to HTML
                            with open(input_file_path, 'r', encoding='utf-8') as f:
                                html = markdown.markdown(f.read())

                            # Write the HTML to a temporary file
                            temp_file_path = os.path.join(output_path, 'temp.html')
                            with open(temp_file_path, 'w', encoding='utf-8') as f:
                                f.write(html)

                            # Convert the HTML to a PDF using pdfkit
                            from_file(temp_file_path, output_file_path, configuration=config,options={"enable-local-file-access": ""})
                            # Delete the temporary HTML file
                            os.remove(temp_file_path)
                except:
                            print("error")

    print('Conversion complete!')
  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()

