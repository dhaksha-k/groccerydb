import cv2

def process_image(file_path):
    # Load the image
    img = cv2.imread(file_path)
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Initialize ORB
    orb = cv2.ORB_create()
    # Find keypoints and descriptors
    keypoints, descriptors = orb.detectAndCompute(gray, None)
    # Further processing and logic to find matches
    return descriptors
