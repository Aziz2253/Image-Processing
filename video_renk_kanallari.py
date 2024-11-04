import cv2 as cv
import numpy as np

#Video giriş ve çıkışı
input_video=r'data/video1.mp4'
output_video=r'data/car_output2.mp4'

#Video Yakalama
cap=cv.VideoCapture(input_video)

#Video özelliklerine bakma
fourcc=cv.VideoWriter_fourcc(*'mp4v') #kodek

# fps= saniyedeki video karesi
fps=int(cap.get(cv.CAP_PROP_FPS)) #saniyedeki frame sayısı
width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH))#genişlik
height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))#yükseklik

#kodek=int(cap.get(cv.CAP_PROP_FOURCC))
# alternatif olarak üstteki satır da kullanılabilir
#coder-decoder =Video okurken boyutu küçültmek amacıyla sıkıştırıp-çözme işlemini uygular
 


#Video oluşturma	
out=cv.VideoWriter(output_video,fourcc,fps,(width,height))# videoyu belirtilen özelliklerde oluşturur

while cap.isOpened():

	ret,frame=cap.read() # cap.read() okunan görüntüyü alır
	#ret, True veya False değerini döndürür. Eğer kare başarıyla okunmuşsa True, aksi durumda False döner.
	#ret, döngülerde videonun sona gelip gelmediğini veya kamerada hata olup olmadığını kontrol etmek için kullanılır.
	#frame, okunan kareyi temsil eder. Bu kare bir NumPy dizisi olarak gelir
	
	if not ret: # sona geldiyse veya hata varsa
		break

	#renk kanallarını al
	b,g,r=cv.split(frame)

	#renk kanallarını birleştir ve maviye çevir
	rgb_frame=cv.merge((g,r,b))
	cv.imshow("Mavi video",rgb_frame)

	out.write(rgb_frame)#videoya yaz

	if cv.waitKey(1) & 0xFF==ord('q'):
		break

cap.release()#bırak
out.release()
cv.destroyAllWindows()


