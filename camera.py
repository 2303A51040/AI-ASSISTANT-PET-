import cv2

class Camera:
    def __init__(self, index=0, width=640, height=480):
        self.cap = cv2.VideoCapture(index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def read(self):
        if not self.cap.isOpened():
            raise RuntimeError("Camera could not be opened. Check CAMERA_INDEX and permissions.")
        ok, frame = self.cap.read()
        if not ok:
            raise RuntimeError("Could not read a frame from the camera.")
        return frame

    def release(self):
        self.cap.release()
