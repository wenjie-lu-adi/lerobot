import cv2

# TODO: Generate a grid live view of available cameras


# def list_available_cameras(max_cameras=5):
#     available_cameras = []
#     for index in range(max_cameras):
#         # Save the current file descriptors
#         sys.stdout.flush()
#         sys.stderr.flush()
#         old_stdout_fd = os.dup(sys.stdout.fileno())
#         old_stderr_fd = os.dup(sys.stderr.fileno())

#         # Redirect stdout and stderr to /dev/null
#         with open(os.devnull, "w") as devnull:
#             devnull_fd = devnull.fileno()
#             os.dup2(devnull_fd, sys.stdout.fileno())
#             os.dup2(devnull_fd, sys.stderr.fileno())

#         try:
#             cap = cv2.VideoCapture(index)
#             if cap is not None and cap.isOpened():
#                 available_cameras.append(index)
#                 cap.release()
#         finally:
#             # Restore stdout and stderr
#             os.dup2(old_stdout_fd, sys.stdout.fileno())
#             os.dup2(old_stderr_fd, sys.stderr.fileno())
#             os.close(old_stdout_fd)
#             os.close(old_stderr_fd)
#     return available_cameras


# cameras = list_available_cameras()
# print("Available camera indices:", cameras)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the webcam.")
else:
    print("Press 'q' to exit the live preview.")

window_name = "Live Preview"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 640, 480)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Display the frame in a window
    cv2.imshow(window_name, frame)

    # Press 'q' to exit the preview window
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
