class CentroidTracker:
    """Very small nearest-centroid tracker for demo use; not robust multi-object tracking."""
    def __init__(self, max_distance=70):
        self.max_distance = max_distance
        self.centres = {}
        self.next_id = 1

    def update(self, boxes):
        results, used = [], set()
        for box in boxes:
            x, y, w, h = map(int, box)
            centre = (x + w // 2, y + h // 2)
            best_id, best_dist = None, self.max_distance
            for object_id, old in self.centres.items():
                if object_id in used:
                    continue
                dist = ((centre[0]-old[0])**2 + (centre[1]-old[1])**2)**0.5
                if dist < best_dist:
                    best_id, best_dist = object_id, dist
            if best_id is None:
                best_id = self.next_id
                self.next_id += 1
            self.centres[best_id] = centre
            used.add(best_id)
            results.append({"id": best_id, "box": (x, y, w, h)})
        self.centres = {k:v for k,v in self.centres.items() if k in used}
        return results
