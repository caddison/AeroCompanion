# Aero Companion

Welcome to the repository for [**Aero Companion!**](https://github.com/caddison/AeroCompanion/wiki) This project is dedicated to creating an autonomous drone that boasts cutting-edge capabilities including real-time video streaming, computer vision, and GPS-independent navigation. Below you will find an in-depth overview of the project, including its components and functionalities. 


---

## Project Overview

This project leverages the capabilities of the Raspberry Pi 5 and Pixhawk 6X flight controller to create a cutting-edge drone capable of executing complex autonomous tasks. The drone is designed to operate without GPS, utilizing IMU data and computer vision for navigation.

---

## Key Features

### Autonomous Flight Control
- Utilizes the **Pixhawk 6X** flight controller for precise and reliable flight control.
- Implements AI models developed in Python to handle autonomous navigation and decision-making.

### Real-Time Video Streaming
- Streams live video feed from the drone's 12MP camera to a web application or **Vuzix Blade** smart glasses for FPV (First Person View) experience.
- Provides video transmission over a **Sixfab 4G/LTE cellular modem** for extended range operations.

### Computer Vision and Obstacle Avoidance
- Employs a secondary downward-facing camera for movement tracking and obstacle detection.
- Integrates computer vision algorithms for target tracking, obstacle avoidance, and payload delivery.

### GPS-Free Navigation
- Relies on IMU data and visual tracking for navigation, ensuring continued operation even in GPS-denied environments.

### Modular Design
- Features a modular payload system allowing for easy swapping of sensors and equipment based on mission requirements.
- Designed for versatility, making it suitable for various applications such as surveillance, delivery, and environmental monitoring.

### Enhanced User Interface
- Provides a web-based control interface compatible with mobile devices, featuring joystick controls and voice command capabilities.
- Integrates with **Vuzix Blade AR smart glasses** to offer augmented reality overlays and voice command input.

---

## Technical Specifications

- **Flight Controller**: Pixhawk 6X
- **Processor**: Raspberry Pi 5
- **Camera**: Raspberry Pi Camera
- **Connectivity**: Sixfab 4G/LTE Cellular Modem
- **Materials**: Lightweight and durable 3D-printed mounts and frames

---

## Useful Commands
These commands are designed for a wide range of commercial applications and allow users to utilize the drone for tasks such as inspection, delivery, and surveillance in various industries:

**Move Up / Move Down**: Vertical navigation for getting the drone to the required altitude.

**Pan Left / Pan Right**: Adjust the drone’s orientation for full 360-degree coverage.

**Move Forward / Move Backward**: Basic forward or backward movement for navigating environments.

**Move Left / Move Right**: Rotate the drone to adjust the camera or sensors without changing position.

**Hover**: Stabilize the drone in one place for a detailed inspection or data capture.

**Track**: Automatically follow a moving object, such as a person or vehicle, based on real-time visual data.

**Follow Route**: Pre-program a route using GPS for the drone to follow autonomously.

**Deliver Package**: Navigate to a specific location and release a payload.

**Return to Home**: Command the drone to return to its launch point.

**Capture Data**: Record visual data for later analysis or real-time transmission to the user.

---

![Screenshot by Snip My on Mar 11, 2025 at 6 53 37 PM](https://github.com/user-attachments/assets/40c38042-9fb9-4730-be62-b61217587c8f)

![Screenshot by Snip My on Mar 11, 2025 at 6 54 10 PM](https://github.com/user-attachments/assets/5c073916-cd7d-455c-aa19-a58c9d2946de)

![Screenshot by Snip My on Mar 11, 2025 at 6 54 40 PM](https://github.com/user-attachments/assets/6540e592-11e4-4d31-8834-54c7459f7597)

![Screenshot by Snip My on Mar 11, 2025 at 6 55 26 PM](https://github.com/user-attachments/assets/cf566c4a-57b7-4643-a2d7-f347da3bb72d)

![Screenshot by Snip My on Mar 11, 2025 at 6 55 49 PM](https://github.com/user-attachments/assets/53867f50-8075-4b4a-ae29-7ddaee4b8605)
