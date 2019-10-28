import os
import fitz

path = '/home/ddwork/projects/201910220145/useless'
pf = fitz.open()
file_list = os.listdir(path)
for img in file_list:  # 读取图片，确保按文件名排序
    if img.endswith('.png'):
        imgdoc = fitz.open(path+'/'+img)  # 打开图片
        pdfbytes = imgdoc.convertToPDF()  # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        pf.insertPDF(imgpdf)  # 将当前页插入文档
pf.save(path+"/new.pdf")  # 保存pdf文件
pf.close()