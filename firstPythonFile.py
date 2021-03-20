# PDF FILE COMBINER
import PyPDF2
pdf1 = input('Input pdf 1: ')
print('\n')
pdf2 = input('Input pdf 2: ')
print('\n')
outputPdf = input('Name New Pdf's Name: ')
def pdf(x):
	pdfObj= open(x,'rb')
	pdfReader= PyPDF2.PdfFileReader(pdfObj)
	return pdfReader
	# This returns a list 

pdfReader1 = pdf(pdf1)
pdfReader2 = pdf(pdf2)
# pdfObj1= open(pdf1,'rb')
# pdfObj2= open(pdf2,'rb')
# pdfReader1= PyPDF2.PdfFileReader(pdfObj1)
# pdfReader2= PyPDF2.PdfFileReader(pdfObj2)
pdfWriter = PyPDF2.PdfFileWriter()


for i in range(pdfReader1.numPages):
	pageObj1=pdfReader1.getPage(i)
	pdfWriter.addPage(pageObj1)

for i in range(pdfReader2.numPages):
	pageObj2=pdfReader2.getPage(i)
	pdfWriter.addPage(pageObj2)
pdfOutputFile =open(outputPdf,'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
# This part below has a bug!
pdfObj1.close()
pdfObj2.close()
