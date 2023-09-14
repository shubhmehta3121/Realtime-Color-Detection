import cv2

# Initialize the video capture object for the default camera (0) or mobile camera
cap = cv2.VideoCapture('0')  # Use '0' for the default camera or provide a URL for a mobile camera

# Set the screen dimensions
screen_width = 1200
screen_height = 800

# Create a resizable window for displaying the webcam feed
cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Webcam", screen_width, screen_height)

while True:
    # Read a frame from the camera
    success, frame = cap.read()

    # Exit the loop if reading fails
    if not success:
        break

    # Resize the frame to the desired screen dimensions
    frame = cv2.resize(frame, (screen_width, screen_height))

    # Flip the frame horizontally (mirror effect)
    mirrored_frame = cv2.flip(frame, 1)

    # Optionally, resize the mirrored frame to a specific size (e.g., 800x600)
    new = cv2.resize(mirrored_frame, (800, 600))

    # Display the mirrored frame in the "Webcam" window
    cv2.imshow("Webcam", mirrored_frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
