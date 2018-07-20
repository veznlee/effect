__author__ = "WSX"
import cv2 as cv
import numpy as np

def local_threshold(img):  #局部阈值
    gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)  #首先变为灰度图
    binary = cv.adaptiveThreshold( gray ,255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY, 25 , 10,)#255 最大值
    #上面的 有两种方法ADAPTIVE_THRESH_GAUSSIAN_C （带权重的均值）和ADAPTIVE_THRESH_MEAN_C（和均值比较）
    #blockSize 必须为奇数 ，c为常量（每个像素块均值 和均值比较 大的多余c。。。少于c）
    #ret 阈值 ， binary二值化图像
    cv.imshow("binary", binary)
    return binary

def jinzita( level ,img ):
    temp = img.copy()
    level = level
    pyr_img = []
    for i in range(level):
        dst = cv.pyrDown( temp )  #pyrup 和pyrDown 相反
        temp = dst.copy()
    return temp

def result(binary):
    w , h = binary.shape[:2]
    print(binary)
    print(w,h)

    with open("result.txt", "w") as f: #初始化文件
        f.write("")
        f.close()
    with open("result.txt","r+") as f:
        for i in range(w):
            for j in range(h):
                if binary[i,j] == 0:
                    temp = "●"
                elif binary[i,j] == 255:
                    temp = "○"
                f.write(temp)
            f.write("\r\n")
        f.close()
    #print(temp.shape)
def main():
    img = cv.imread("1.JPG")
    #cv.namedWindow("Show", cv.WINDOW_AUTOSIZE)
    cv.imshow("Show", img)
    t = jinzita(3, img)
    binary=local_threshold(t)
    result(binary)
    cv.waitKey(0)
    cv.destroyAllWindows()

main()