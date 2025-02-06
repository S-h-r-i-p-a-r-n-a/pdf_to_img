from pdf2image import convert_from_path

old_pdf = convert_from_path("Python Roadmap.pdf",
                            poppler_path=r"C:\Users\User\OneDrive\Desktop\python\poppler-24.08.0\Library\bin")
for i in range(len(old_pdf)):
    old_pdf[i].save("new"+str(i)+".jpg","JPEG")    

