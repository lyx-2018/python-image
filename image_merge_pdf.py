import os
from PIL import Image

path = r'U:/201910250420/Trademark/商标详情页截图'   #图片文件夹
pdf_name = '商标截图.pdf'  #生成的PDF 路径
png_list = os.listdir(path)
im1 = Image.open(path+'/'+png_list[0])
if im1.mode == "RGBA":
   im1 = im1.convert('RGB')
png_list.pop(0)
im_list = []
for i in png_list:
    img = Image.open(path+'/'+i)
    if img.mode == "RGBA":
        new_img = img.convert('RGB')
        im_list.append(new_img)
    else:
        im_list.append(img)
im1.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=im_list)
print("输出文件名称：", pdf_name)