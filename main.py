import http_listener as hl
import cv2
import time

start = True

# Start the http server
hl.start_server()

while start:
    # wait 100 ms
    time.sleep(0.1)
    # print('Started')
    if hl.start_state:
        # Capture video from camera
        cap = cv2.VideoCapture(0)

        # Check if camera is opened
        if not cap.isOpened():
            print("Error opening video stream or file")

        # Read until video is completed
        while cap.isOpened():
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret:
                # Display the resulting frame
                cv2.imshow('Frame', frame)
                # Press Q on keyboard to  exit
                if cv2.waitKey(5) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    cap.release()
                    break
            # Break the loop
            else:
                break

            if not hl.start_state:
                break
        
        print('exit while')
        # Destroy all windows
        cv2.destroyAllWindows()
        # Release the video capture object
        cap.release()

