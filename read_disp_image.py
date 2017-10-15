import cv2

image = cv2.imread("/home/hadoop/Downloads/e-commerce-7-638.jpg")
print type(image)

cv2.imshow('test image', image)
cv2.waitkey(0)
cv2.destroyallWindows()
