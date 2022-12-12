from time import sleep
from picamera import PiCamera
camera = PiCamera()

camera.annotate_text = "Vinicius Costa 11300068 \n M.R.Valentini 11300030"
camera.capture('sel0337.jpg')
camera.resolution = (512, 384)
camera.start_preview()
sleep(5)
camera.stop_preview()
  