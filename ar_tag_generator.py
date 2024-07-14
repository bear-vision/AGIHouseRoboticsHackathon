import cv2
import cv2.aruco as aruco
import time

def generate_ar_tag(seconds):
    dictionary = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
    marker_id = seconds % 50  # Using seconds as marker ID
    marker_size = 200  # 200x200 pixels
    marker_image = aruco.generateImageMarker(dictionary, marker_id, marker_size)
    return marker_image

def ar_tag_generation():
    while True:
        current_time = time.localtime()
        seconds = current_time.tm_sec + 10
        ar_tag = generate_ar_tag(seconds)
        cv2.imshow('AR Tag', ar_tag)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(1) 
        
if __name__ == "__main__":
    ar_tag_generation()
