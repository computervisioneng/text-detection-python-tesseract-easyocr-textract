import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

# read image
image_path = './test.png'

img = cv2.imread(image_path)

# instance text detector
reader = easyocr.Reader(['en'], gpu=False)

# detect text on image
text_ = reader.readtext(img)

threshold = 0.25
# draw bbox and text
for t_, t in enumerate(text_):
    print(t)

    bbox, text, score = t

    if score > threshold:
        cv2.rectangle(img, [int(j) for j in bbox[0]], [int(j) for j in bbox[2]], (0, 255, 0), 15)
        cv2.putText(img, text, [int(j) for j in bbox[0]], cv2.FONT_HERSHEY_COMPLEX, 2.5, (0, 0, 255), 5)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
