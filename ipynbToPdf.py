import notebook_as_pdf

# Specify the path to your IPYNB file
notebook_path = '/home/dev/Desktop/Machine-Learning-Lab/Assignment-02-UDF/Multi Linear Regression/Model.ipynb'

# Optional: Set output path for the PDF file (defaults to same directory as notebook)
output_path = "MLR Model.pdf"

try:
    # Convert the notebook to PDF
    notebook_as_pdf.convert_notebook(notebook_path, output_path=output_path)
    print("Notebook successfully converted to PDF!")
except Exception as e:
    print("Error converting notebook:", e)

