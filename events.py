import json, time
from shared.config import MQTT_ENABLED, MQTT_HOST, MQTT_PORT, MQTT_TOPIC

_client = None

def publish_event(event_type: str, payload: dict) -> bool:
    """Publish a JSON event if MQTT is enabled; otherwise print it locally."""
    global _client
    message = {"source": "nexus", "type": event_type, "timestamp": time.time(), "data": payload}
    if not MQTT_ENABLED:
        print("[NEXUS EVENT]", json.dumps(message))
        return False
    try:
        import paho.mqtt.client as mqtt
        if _client is None:
            _client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
            _client.connect(MQTT_HOST, MQTT_PORT, 60)
            _client.loop_start()
        _client.publish(MQTT_TOPIC, json.dumps(message), qos=0)
        return True
    except Exception as exc:
        print(f"[MQTT unavailable] {exc}")
        return False
