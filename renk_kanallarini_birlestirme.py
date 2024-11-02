import cv2 as cv

img_bgr=cv.imread("data/elma.jpg")

cv.imshow("Red Apple",img_bgr)


b,g,r=cv.split(img_bgr)

#kırmızı ve yeşil kanalları birleştir
img_yesil=cv.merge((b,r,g))
cv.imshow("Green Apple",img_yesil)


img_yellow=cv.merge((b,r,r))
cv.imshow("Yellow Apple",img_yellow)


cv.waitKey(0)
cv.destroyAllWindows()
