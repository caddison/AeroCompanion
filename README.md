# Aero Companion

Welcome to the repository for [**Aero Companion!**](https://github.com/caddison/AeroCompanion/wiki) This project aims to develop an autonomous drone equipped with advanced features such as real-time video streaming, computer vision, and GPS independent navigation. Below is a detailed overview of the project, its components, and functionalities.

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

## How It Works

The drone operates using a combination of IMU data, computer vision, and AI algorithms. The AI model processes real-time telemetry data and user commands, executing complex maneuvers and maintaining stable flight. The drone streams live video to the user's web application or AR smart glasses, providing a real-time FPV experience and enabling remote operation.

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

## Getting Started

To get started with this project, clone the repository and follow the setup instructions provided in the `README.md`. Detailed documentation and tutorials are available to guide you through the installation, configuration, and operation of the drone.

---

## Contributions

We welcome contributions from the community! Feel free to fork the repository, submit pull requests, and report issues. For major changes, please open an issue first to discuss your ideas.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

We hope you find this project interesting and look forward to your contributions and feedback!


