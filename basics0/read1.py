import cv2 as cv
#code for reading images
'''
img = cv.imread('C:\\opencv-learning\\resources\\photos\\cat_large.jpg')

cv.imshow('Cat', img)
cv.waitKey(0) #waits for a key to be pressed
'''
# code for reading videos
capture = cv.VideoCapture('C:\\opencv-learning\\resources\\videos\\dog.mp4')
while True:
    isTrue, frame = capture.read()#reads the video frame by frame
    cv.imshow('Video',frame)

    if not isTrue:
        break

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()