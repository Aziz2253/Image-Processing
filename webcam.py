import cv2 as cv

#kameradan görüntü al

cap=cv.VideoCapture(0) # 0 varsayılan kamera

while True:
	ret,frame=cap.read()

	if not ret:
		break
	
	gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
	cv.imshow('Siyah-Beyaz Kanali',gray_frame)

	hsv_img=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
	cv.imshow('HSV Kanali',hsv_img)

	hls_img=cv.cvtColor(frame,cv.COLOR_BGR2HLS) 
	cv.imshow('HLS Kanali',hls_img)

	rgba_img=cv.cvtColor(frame,cv.COLOR_BGR2RGBA)
	cv.imshow('RGBA Kanali',rgba_img)

	rgb_img=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
	cv.imshow('RGB Kanali',rgb_img)
	

	#Görüntüyü çevirme
	flipped_img=cv.flip(frame,1) #0 dikey , 1 yatay, -1 de tersine çevirme
	cv.imshow('Kamera Org',frame)
	cv.imshow('Cevirilmis',flipped_img)
	 

	if cv.waitKey(1) & 0xFF==ord('q'):
		break

	
#kamerayı kapat
cap.release()
cv.destroyAllWindows()