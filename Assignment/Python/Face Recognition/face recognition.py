import cv2

# Loading The Cascade File
face_cascade = cv2.CascadeClassifier(r'D:\\paras\\Assignment\\python\\Face Recognition\\haarcascade_frontalface_default.xml')

# Reading the Input Image (you can change this to p1.png or rdj.jpg as needed)
image_path = r'D:\\paras\\Assignment\\python\\Face Recognition\\p1.png'  # Change to rdj.jpg if needed
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load image. Check the file path.")
else:
    # Resizing the Image
    img = cv2.resize(image, None, fx=0.3, fy=0.3)

    # Converting the image into grayscale image
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecting The Faces
    faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

    # Pointing The Faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Displaying The Output Image
    cv2.imshow('img', img)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close all OpenCV windows
