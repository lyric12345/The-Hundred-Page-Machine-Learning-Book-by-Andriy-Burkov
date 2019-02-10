import glob
from PyPDF2 import PdfFileMerger, PdfFileReader

def main():
    pdfs = glob.glob("*.pdf")  #Make a list of all pdf files in the directory
    print(pdfs)

    merger = PdfFileMerger()

    merger.append(fileobj = open(pdfs[0], "rb"))  #Append 1st chapter(with cover) to the merger 

    for pdf in pdfs[1:]:
        n = PdfFileReader(pdf).getNumPages()
        merger.append(fileobj = open(pdf, "rb"), pages=(2,n))  #Append the rest of the chapters

    output = open("The Hundred Page Machine Learning Book.pdf", "wb")

    merger.write(output)

if __name__ == "__main__":
    main()