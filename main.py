import cv2
from shared.config import CAMERA_INDEX
from shared.events import publish_event
from vision_ai.camera import Camera
from vision_ai.adapters.face import FaceDetector
from vision_ai.adapters.person import PersonDetector
from vision_ai.tracking import CentroidTracker

def main():
    camera = Camera(CAMERA_INDEX)
    faces, people, tracker = FaceDetector(), PersonDetector(), CentroidTracker()
    print("NEXUS Vision AI started. Press q in the video window to quit.")
    try:
        while True:
            frame = camera.read()
            for (x, y, w, h) in faces.detect(frame):
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255,180,0), 2)
                cv2.putText(frame, "Face detected", (x,y-8), cv2.FONT_HERSHEY_SIMPLEX, .5, (255,180,0), 1)
            detections = people.detect(frame)
            tracked = tracker.update([d[0] for d in detections])
            for item in tracked:
                x,y,w,h = item["box"]
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,220,0), 2)
                cv2.putText(frame, f"Person {item['id']}", (x,y-8), cv2.FONT_HERSHEY_SIMPLEX, .5, (0,220,0), 1)
            if detections:
                publish_event("person_detection", {"count": len(detections), "tracks": tracked})
            cv2.imshow("NEXUS Vision AI", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
