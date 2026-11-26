# Hardware Integration Notes

## ESP32
Responsible for low-level sensor and actuator interfacing. Confirm board variant and available pins before wiring.

## Camera
Used as the visual input source. The Python Vision AI baseline expects a webcam accessible to the computer. If using an ESP32 camera, implement a compatible stream/transport adapter.

## Ultrasonic sensor
Use for distance measurement and obstacle-stop input. Verify logic voltage compatibility; many ESP32 GPIO pins are not 5 V tolerant.

## Motor driver and four-wheel platform
Use a motor driver matched to motor stall current. Add a hardware emergency stop and independent obstacle-stop logic. Do not drive motors directly from ESP32 GPIO.

## Battery and converters
Verify cell chemistry, series/parallel arrangement, protection/BMS, fuse, converter ratings, grounding, and thermal limits with a qualified supervisor before powering the robot.

## Display
The included TFT_eSPI sketch is a UI starter only. Configure the library for the exact display controller and wiring.
