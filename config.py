import os
from dotenv import load_dotenv
load_dotenv()

def env_bool(name: str, default=False) -> bool:
    return os.getenv(name, str(default)).strip().lower() in ("1", "true", "yes", "on")

CAMERA_INDEX = int(os.getenv("CAMERA_INDEX", "0"))
DATABASE_PATH = os.getenv("DATABASE_PATH", "nexus.db")
MQTT_ENABLED = env_bool("MQTT_ENABLED", False)
MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "nexus/events")
