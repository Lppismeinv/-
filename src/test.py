# from HmmPosTag import main_H
# import ShortTokenizer
# from paddleocr import PaddleOCR
# import cv2 as cv
# import copy
# # import streamlit as st
# import numpy as np
#
#
# def gama(img):
#     # 读入原始图像
#     # img = cv.imread(imgpath, 1)
#     # 伽马变换
#     gamma = copy.deepcopy(img)
#     rows = img.shape[0]
#     cols = img.shape[1]
#     for i in range(rows):
#         for j in range(cols):
#             gamma[i][j] = 3 * pow(gamma[i][j], 0.8)
#     outimgpath = '../out/gamma4.jpg'
#     cv.imwrite(outimgpath, gamma)
#     return outimgpath
#
#
# if __name__ == '__main__':
#     upload_file = st.file_uploader("请选择一张图片上传", type=['jpg', 'png', 'jpeg'])
#     # 图片预处理，然后输入到模型进行预测
#     if upload_file is not None:
#         image = np.array(bytearray(upload_file.read()), dtype='uint8')  # 读取图片
#         image = cv.imdecode(image, cv.IMREAD_COLOR)  # 字节解码
#         RGB_img = cv.cvtColor(image, cv.COLOR_BGR2RGB)  # 图片通道转换
#         # 显示图片
#         st.markdown("### 用户上传图片，显示如下: ")
#         st.image(RGB_img, channels="RGB")
#         # 对图像进行处理
#         outimg_path = gama(RGB_img)
#         # 显示处理后的图像
#         out_img = cv.imread(outimg_path)
#         st.markdown("### 处理后的图像如下: ")
#         st.image(out_img, channels="RGB")
#         # 文字提取
#         st.markdown("**请点击按钮开始文字提取**")
#         click = st.button("文字提取")
#         if click:
#             # img_path = '../img/test5.jpg'
#             # img = cv.imread(img_path)
#             # img_out = gama(RGB_img)
#             ocr = PaddleOCR(lang='ch')
#             result = ocr.ocr(outimg_path)
#             result = result[0]
#             txts = [line[1][0] for line in result]
#             print("文字提取结果\n", txts)
#             with open("output.txt", "w", encoding="utf-8") as f:
#                 for txt in txts:
#                     f.write(txt + "")
#             st.title(txts)
#             # main_H()
#             # ShortTokenizer.main_S()
from paddleocr import PaddleOCR
import cv2 as cv
import copy
from HmmPosTag import main_H
import ShortTokenizer


def gama(img_path):
    # 读入原始图像
    img = cv.imread(img_path, 1)
    # 伽马变换
    gamma = copy.deepcopy(img)
    rows = img.shape[0]
    cols = img.shape[1]
    for i in range(rows):
        for j in range(cols):
            gamma[i][j] = 3 * pow(gamma[i][j], 0.8)
    img_out = '../out/gamma4.jpg'
    cv.imwrite(img_out, gamma)
    return img_out


if __name__ == '__main__':

    img_path = '../img/test5.jpg'
    img_out = gama(img_path)
    ocr = PaddleOCR(lang='ch')
    result = ocr.ocr(img_out)
    print("文字提取结果\n", result)

    result = result[0]
    txts = [line[1][0] for line in result]
    with open("output.txt", "w", encoding="utf-8") as f:
        for txt in txts:
            f.write(txt + "")
    main_H()
    ShortTokenizer.main_S()
