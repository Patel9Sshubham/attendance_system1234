# import cv2

# cap=cv2.VideoCapture(0)
# ret=True
# while ret:
#     ret, frame=cap.read()
#     x,y,c=frame.shape

# import the opencv library
import cv2


# define a video capture object
vid = cv2.VideoCapture(0)

while(True):
	
	# Capture the video frame
	# by frame
	ret, frame = vid.read()

	# Display the resulting frame
	cv2.imshow('frame', frame)
	
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
    # file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
    # cv2.imwrite(file_name_path,face)
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

