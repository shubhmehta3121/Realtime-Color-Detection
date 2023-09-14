import cv2
import numpy as np
import stack_multi_utils


# Callback function for trackbars
def empty():
    pass


# Initialize the video capture object
cap = cv2.VideoCapture(0)
# Alternatively, you can use a mobile camera by uncommenting the line below
# cap = cv2.VideoCapture('https://192.168.1.104:8080/video')

# Set the screen dimensions
screen_width = 400
screen_height = 400

# Create an HSV window
cv2.namedWindow("HSV", cv2.WINDOW_NORMAL)
cv2.resizeWindow("HSV", screen_width, screen_height)

# Create trackbars for adjusting HSV values
cv2.createTrackbar('HUE MIN', 'HSV', 0, 179, empty)
cv2.createTrackbar('HUE MAX', 'HSV', 179, 179, empty)
cv2.createTrackbar('SAT MIN', 'HSV', 0, 255, empty)
cv2.createTrackbar('SAT MAX', 'HSV', 255, 255, empty)
cv2.createTrackbar('VALUE MIN', 'HSV', 0, 255, empty)
cv2.createTrackbar('VALUE MAX', 'HSV', 255, 255, empty)

# Main loop for capturing and processing frames
while True:
    success, frame = cap.read()

    if not success:
        break

    # Resize the frame to the desired screen dimensions
    frame = cv2.resize(frame, (screen_width, screen_height))
    mirrored_frame = cv2.flip(frame, 1)

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(mirrored_frame, cv2.COLOR_BGR2HSV)

    # Get the current trackbar positions
    hue_min = cv2.getTrackbarPos('HUE MIN', 'HSV')
    hue_max = cv2.getTrackbarPos('HUE MAX', 'HSV')
    sat_min = cv2.getTrackbarPos('SAT MIN', 'HSV')
    sat_max = cv2.getTrackbarPos('SAT MAX', 'HSV')
    value_min = cv2.getTrackbarPos('VALUE MIN', 'HSV')
    value_max = cv2.getTrackbarPos('VALUE MAX', 'HSV')

    # Define lower and upper HSV thresholds based on trackbar values
    lower = np.array([hue_min, sat_min, value_min])
    upper = np.array([hue_max, sat_max, value_max])

    # Create a mask based on the thresholds
    mask = cv2.inRange(hsv, lower, upper)

    # Apply the mask to the mirrored frame
    results = cv2.bitwise_and(mirrored_frame, mirrored_frame, mask=mask)

    # Stack the original frame, mask, and results side by side
    stacked = stack_multi_utils.stackimages([mirrored_frame, mask, results], 1, 3, 1)

    # Resize the stacked image for display
    new = cv2.resize(stacked, (1200, 800))

    # Display the stacked image
    cv2.imshow("Stacked HSV", new)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
