import cv2 as cv
import numpy as np
import gradio as gr

# Görseli siyah-beyaza dönüştüren fonksiyon
def nostalji(image):
    image = np.array(image)
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)# COLOR_BGR2GRAY fonksiyonu 3 katmanlı imgeyi tek katmanlı hale dönüştürür
    return gray_image

# Gradio arayüzü oluşturma
with gr.Blocks() as demo:
    gr.Markdown("# Görseli Siyah Beyaza Çevir!")
    gr.Markdown("Bir resim yükleyin ve siyah beyaza çevrilsin!")

    image_input = gr.Image(type='pil', label="Girdi Görseli")
    image_output = gr.Image(type="numpy", label="Sonuç Görseli")

    # Bileşenleri fonksiyonla bağlama
    btn = gr.Button("Çevir")
    btn.click(fn=nostalji, inputs=image_input, outputs=image_output)

# Gradio arayüzünü başlatma 
if __name__ == "__main__":
	
    demo.launch(share=True)