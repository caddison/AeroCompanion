# Aero Companion

Welcome to the repository for [**Aero Companion**]!(https://github.com/caddison/AeroCompanion/wiki) This project aims to develop a fully autonomous drone equipped with advanced features such as real-time video streaming, computer vision, obstacle avoidance, and AI-driven navigation. Below is a detailed overview of the project, its components, and functionalities.

---

## Project Overview

This project leverages the powerful capabilities of the Raspberry Pi 5 and Pixhawk 6X flight controller to create a cutting-edge drone capable of executing complex autonomous tasks. The drone is designed to operate without GPS, utilizing IMU data and computer vision for navigation and obstacle avoidance.

---

## Key Features

### Autonomous Flight Control
- Utilizes the **Pixhawk 6X** flight controller for precise and reliable flight control.
- Implements advanced AI models developed in Python to handle autonomous navigation and decision-making.

### Real-Time Video Streaming
- Streams live video feed from the drone's 12MP camera to a web application or **Vuzix Blade** smart glasses for FPV (First Person View) experience.
- Provides seamless video transmission over a **Sixfab 4G/LTE cellular modem** for extended range operations.

### Computer Vision and Obstacle Avoidance
- Employs a secondary downward-facing camera for movement tracking and obstacle detection.
- Integrates computer vision algorithms for target tracking, obstacle avoidance, and payload delivery precision.

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
- **Camera**: Raspberry Pi 12MP HQ Camera
- **Connectivity**: Sixfab 4G/LTE Cellular Modem
- **Power**: Tattu 1050mAh 6S 95C LiPo Battery
- **Materials**: Lightweight and durable 3D-printed mounts and frames

---

## How It Works

The drone operates using a combination of IMU data, computer vision, and AI algorithms. The AI model processes real-time telemetry data and user commands, executing complex maneuvers and maintaining stable flight. The drone streams live video to the user's web application or AR smart glasses, providing a real-time FPV experience and enabling remote operation.

---

## Future Enhancements

- **Swarm Intelligence**: Coordination between multiple drones for advanced missions.
- **Automatic Retraining**: Users can issue a "train" command to process saved telemetry and command data, updating the AI model to improve drone control and performance after each session.
- **Payload Delivery**: Precision payload delivery using computer vision and modular payload systems.

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


