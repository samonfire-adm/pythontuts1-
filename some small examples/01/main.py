import time 
import pyscreenshot


time.sleep(10)

image = pyscreenshot.grab()

image.show()

image.save('Screenshot.png')