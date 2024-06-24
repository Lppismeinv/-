# from paddleocr import PaddleOCR
# import cv2 as cv
# import copy
# from src import test
#
#
# def gama(img_path):
#     # 读入原始图像
#     img = cv.imread(img_path, 1)
#     # 伽马变换
#     gamma = copy.deepcopy(img)
#     rows = img.shape[0]
#     cols = img.shape[1]
#     for i in range(rows):
#         for j in range(cols):
#             gamma[i][j] = 3 * pow(gamma[i][j], 0.8)
#     img_out = './out/gamma4.jpg'
#     cv.imwrite(img_out, gamma)
#     return img_out
#
#
# if __name__ == '__main__':
#
#     img_path = './img/test5.jpg'
#     img_out = gama(img_path)
#     ocr = PaddleOCR(lang='ch')
#     result = ocr.ocr(img_out)
#     print("文字提取结果\n", result)
#
#     result = result[0]
#     txts = [line[1][0] for line in result]
#     with open("output.txt", "w", encoding="utf-8") as f:
#         for txt in txts:
#             f.write(txt + "")
#     test.test_main()
