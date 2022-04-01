import markdown
import pdfkit
from pygments import highlight
from pygments.formatters import HtmlFormatter

def mark_to_html():
    #Read markdown file
    f = open('README.md', mode='r', encoding='UTF-8')
    with f:
        text = f.read()
        #Create stylesheets for highlights with Pygments
        style = HtmlFormatter(style='solarized-dark').get_style_defs('.codehilite')
        # #Markdown → HTML conversion
        md = markdown.Markdown(extensions=['extra', 'codehilite'])
        body = md.convert(text)
        #Fit to HTML format
        html = '<html lang="ja"><meta charset="utf-8"><body>'
        #Import stylesheets created with Pygments
        html += '<style>{}</style>'.format(style)
        #Add style to add border to Table tag
        html += '''<style> table,th,td { 
            border-collapse: collapse;
            border:1px solid #333; 
            } </style>'''
        html += body + '</body></html>'
        return html

def html_to_pdf(html: str):
    #Specifying the output file
    outputfile = './output.pdf'
    #Specifying the path of the wkhtmltopdf executable file
    # path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(
        # wkhtmltopdf=path_wkhtmltopdf
        )
    #Perform HTML → PDF conversion
    pdfkit.from_string(html, outputfile, configuration=config)

if __name__=='__main__':
    html = mark_to_html()
    html_to_pdf(html)
