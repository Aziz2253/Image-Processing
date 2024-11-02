import cv2 as cv

img=cv.imread('data/yesil_elma.jpg')

# görüntünün boyutları 
print(cv.__version__)

print(img)
print(img.shape)

# listedeki ilk eleman yüksekligi, ikinci eleman genisligi, ücüncü eleman ise kanal sayısını verir
height,width=img.shape[:2]
print("Yüksekliği :",img.shape[0])

print("Genişliği :",img.shape[1])

print("Kanal sayısı :",img.shape[2])

print("Veri tipi :",img.dtype)

# resmi göster
cv.imshow("Yesil Elma",img)
cv.waitKey(0)
cv.destroyAllWindows()



