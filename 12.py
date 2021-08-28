# importing required modules
import PyPDF2


def PDFmerge(pdfs, output):
	# creating pdf file merger object
	pdfMerger = PyPDF2.PdfFileMerger()

	# appending pdfs one by one
	for pdf in pdfs:
		pdfMerger.append(pdf)

	# writing combined pdf to output pdf file
	with open(output, 'wb') as f:
		pdfMerger.write(f)


def main():
	# pdf files to merge
	pdfs = ['c:/py-practice-os/example.pdf', 'c:/py-practice-os/rotated_example.pdf']

	# output pdf file name
	output = 'combined_example.pdf'

	# calling pdf merge function
	PDFmerge(pdfs=pdfs, output=output)


if __name__ == "__main__":
	# calling the main function
	main()
