import cv2
# capturing video using cv2 library with videocapture function and parameter 0 because 0 is the index for webcam of pc
video=cv2.VideoCapture(0)
# giving the first frame that captured as none
first_frame=None
while True:
    check,frame=video.read()
    # gray scale: to increase the accuracy of motion detection
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # blur the image to smoothen the detection
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        # first frame is converted into gray scale as reference frame
        first_frame=gray
        # now we will continue as the while loop starts executing again
        continue
    # first_frame is compared to the next frames coming so we are using absolute difference function
    delta_frame=cv2.absdiff(first_frame,gray)
    # threshold to not to detect noises etc
    threshold=cv2.threshold(delta_frame,50,255,cv2.THRESH_BINARY)[1]
    # dilate function to smoothen the frame more and we will keep iterations low because if it is more it will detect noises
    threshold=cv2.dilate(threshold,None,iterations=2)
    # Contours are points at which motion is happening. So we will find contours
    (cntr,_)=cv2.findContours(threshold.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
   
    # specifying the contour width
    for contour in cntr:
        # we dont consider this area as motion area
        if cv2.contourArea(contour)<1000:
            continue
        # bounding contour area width rectangle
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    
    # displaying the window
    cv2.imshow("display",frame)
    # for exit criteria
    key=cv2.waitKey(1)
    # if we press 'e' the window will break
    if key==ord('e'):
        break

video.release()
cv2.destroyAllWindows()


