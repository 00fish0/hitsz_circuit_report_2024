# -*encoding:gbk*-
from PyPDF2 import PdfFileReader, PdfFileWriter

# �г�����Ҫƴ�ӵ�PDF�ļ�
pdf_files = ['pdf1.pdf','pdf2.pdf']
pdf_writer = PdfFileWriter()

for pdf_file in pdf_files:
    # ��PDF�ļ�
    f = open(pdf_file, 'rb')
    pdf_reader = PdfFileReader(f)
    # ��ÿһҳ��ӵ�PdfFileWriter������
    if pdf_file==pdf_files[0]:
        for page_num in range(2):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)
    else:
        for page_num in range(2,pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

# д�뵽һ���µ�PDF�ļ���
with open('merged.pdf', 'wb') as out:
    pdf_writer.write(out)

