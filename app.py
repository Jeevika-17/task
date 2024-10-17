from flask import Flask, request, render_template, send_file
import pdfkit
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_to_pdf():
    url = request.form.get('url')
    
    try:
        # Generate PDF from URL
        pdf_path = 'website.pdf'
        pdfkit.from_url(url, pdf_path)

        # Send the PDF file as an attachment
        return send_file(pdf_path, as_attachment=True)

    except Exception as e:
        return f"Error generating PDF: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
