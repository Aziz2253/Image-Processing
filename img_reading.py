import cv2 as cv

image_path=r'data/satranc3x3.jpg'

orj_img=cv.imread(image_path,cv.IMREAD_COLOR) # cv.IMREAD_COLOR yerine 1 yazsak yine aynı görüntüyü elde ederiz
cv.imshow('Renkli Satranc 3x3', orj_img)

img_gray=cv.imread(image_path,cv.IMREAD_GRAYSCALE) # cv.IMREAD_GRAYSCALE yerine 0 yazsak yine aynı görüntüyü elde ederiz
cv.imshow('Gri Satranc 3x3', img_gray)


image_path2=r'data/yesil_elma.jpg'

renkli_elma=cv.imread(image_path2,cv.IMREAD_COLOR)
cv.imshow('Renkli Elma', renkli_elma)

gray_elma=cv.imread(image_path2,cv.IMREAD_GRAYSCALE)
cv.imshow('Gri Elma', gray_elma)


cv.waitKey(0) #pencerenin açık kalmasını sağlar herhangi bir tuşa basılınca kapanır
cv.destroyAllWindows()