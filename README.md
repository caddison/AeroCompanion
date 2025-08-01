# Aero Companion System Architecture

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange.svg)](https://ultralytics.com)
[![MAVLink](https://img.shields.io/badge/MAVLink-2.0-red.svg)](https://mavlink.io)

**Phase 1**: Implementing semi-autonomous capabilities with manned pilots controlling drones through user-friendly web applications.


Welcome to the repository for [**Aero Companion!**](https://github.com/caddison/AeroCompanion/wiki) This project is dedicated to creating an autonomous drone that boasts cutting-edge capabilities including real-time video streaming, computer vision, and GPS-independent navigation. 

![image0](https://github.com/user-attachments/assets/a31faa19-307c-4796-b84e-6b28c898660d)

---


## Project Overview

This project leverages the capabilities of the Raspberry Pi 5 and Pixhawk 6X flight controller to create a cutting-edge drone capable of executing complex autonomous tasks. The drone is designed to operate without GPS, utilizing IMU data and computer vision for navigation.

---

## Key Features

### Autonomous Flight Control
- Utilizes the **Pixhawk 6X** flight controller for precise and reliable flight control.
- Implements AI models to handle autonomous navigation and decision-making.

### Real-Time Video Streaming
- Streams live video feed from the drone's camera to a web application or **Vuzix Blade** smart glasses for FPV (First Person View) experience.
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

<img width="810" height="500" alt="skynet" src="https://github.com/user-attachments/assets/5eef0489-0114-42ab-bbf5-18ba931d37fe" />



# Autonomous System Architecture

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange.svg)](https://ultralytics.com)
[![MAVLink](https://img.shields.io/badge/MAVLink-2.0-red.svg)](https://mavlink.io)

**Phase 2**: Transitioning from command-based manual operation to fully autonomous, modular system with USB mission profiles.

An intelligent drone system that reads mission objectives from USB and executes autonomous operations using computer vision, SLAM navigation, and safety monitoring.

## System Overview

```mermaid
graph TD
    A[Mission Controller] --> B[Flight Interface]
    A --> C[SLAM Navigation]
    A --> D[Computer Vision]
    A --> E[Command Interpreter]
    A --> F[Safety Monitor]
    A --> G[Data Logger]
    
    B --> H[ArduPilot]
    C --> I[Bottom Camera]
    D --> J[Forward Camera]
    F --> K[Emergency RTL]
    G --> L[USB Storage]
```

## Core Modules

### 1. Mission Controller

**Purpose:** Central coordinator that orchestrates all other modules

**Key Responsibilities:**
- Parse Program Objectives from USB
- Maintain mission state machine
- Coordinate all modules
- **Priority**: Safety > Mission > Efficiency

---

### 2. Flight Interface Module

**Purpose:** Handles MAVLink communication with ArduPilot

**Features:**
- Real-time telemetry (GPS, battery, attitude)
- Flight mode control
- MAVLink command handling
- Safety parameter enforcement

---

### 3. SLAM Navigation Module

**Purpose:** Tracks position via visual SLAM using bottom-facing camera and AI HAT+

**Capabilities:**
- ORB-SLAM implementation
- Home position reference
- Drift detection

---

### 4. Computer Vision Module

**Purpose:** Detects and tracks objects using AI HAT+

**Intelligence:**
- Real-time YOLOv8n inference
- Object tracking
- Distance estimation

---

### 5. Command Interpreter Module

**Purpose:** Converts high-level commands into drone actions

**Supported Commands:**

| Command | Description | Use Case |
|---------|-------------|----------|
| `hover` | Maintain position using computer vision | Stable observation |
| `track` | Follow object at defined distance | Wildlife monitoring |
| `guard` | Circle/patrol an area | Perimeter security |
| `find` | Search pattern for specific target | Search & rescue |
| `surveil` | Observe area/object for duration | Surveillance ops |
| `recon` | Map and scan defined region | Area mapping |
| `goto` | Navigate to coordinates | Waypoint missions |
| `return` | Return home using SLAM/GPS | Mission completion |

---

### 6. Safety Monitor Module

**Purpose:** Continuous safety and health monitoring

**Safety Features:**
- Smart battery reserve calculation
- Geofence boundary enforcement
- System health monitoring
- Automatic emergency RTL

---

### 7. Data Logger Module

**Purpose:** Mission telemetry and data recording

**Data Management:**
- Timestamped event logging
- Flight path and telemetry logs
- Mission reports

## Mission Configuration

### Program Objectives File Format

Missions are defined in JSON format on USB drive:

```json
{
  "mission_id": "wildlife_survey_001",
  "metadata": {
    "created": "2024-07-24T10:30:00Z",
    "operator": "research_team",
    "location": "yellowstone_sector_7"
  },
  "parameters": {
    "max_flight_time": 1200,     
    "battery_reserve": 20,       
    "max_altitude": 50,          
    "track_distance": 15,        
    "geofence_radius": 500       
  },
  "objectives": [
    {
      "command": "find",
      "target": "bird",
      "area": "circle",
      "radius": 100,
      "timeout": 300,
      "priority": "high"
    },
    {
      "command": "track",
      "duration": 180,
      "distance": 15,
      "record_video": true,
      "follow_mode": "adaptive"
    },
    {
      "command": "surveil",
      "duration": 120,
      "area": "current_position",
      "altitude": 30
    },
    {
      "command": "return",
      "method": "slam_primary"
    }
  ]
}
```

## System Flow

### Startup Sequence

```
1. Boot & Initialize → Load modules & connect flight controller
2. Mission Load → Parse objectives from USB
3. Pre-Flight Check → Verify all systems green
4. SLAM Initialize → Set home position reference
5. Takeoff → Begin mission at safe altitude
```

### Mission Loop

- **Continuous Monitoring**: Safety & health checks every 100ms
- **Objective Processing**: Parse and execute mission commands
- **Sensor Fusion**: SLAM + GPS + vision integration  
- **Data Recording**: Log all events and telemetry
- **Decision Making**: Adaptive behavior based on conditions

### Emergency Handling

| Trigger | Response | Fallback |
|---------|----------|----------|
| Low Battery | Immediate RTL | Critical landing |
| SLAM Failure | GPS-only mode | Manual override |
| Geofence Breach | Forced return | Emergency stop |

## Development Roadmap

### Phase 1: Foundation *(Completed)*
- [x] Flight Interface Module
- [x] Basic Mission Controller  
- [ ] Safety Monitor Framework

### Phase 2: Navigation *(Current Phase)*
- [ ] SLAM Navigation Module
- [x] Command Interpreter
- [x] USB Program Objectives Parser
- [ ] Integration testing

### Phase 3: Intelligence
- [x] Computer Vision Module (YOLOv8)
- [ ] Advanced command implementations
- [x] Data Logger with analytics
- [ ] Machine learning integration

### Phase 4: Field Testing 
- [ ] Full module integration
- [ ] Real-world field testing
- [ ] Emergency scenario simulation
- [ ] Performance optimization



# Agentic System Architecture

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange.svg)](https://ultralytics.com)
[![MAVLink](https://img.shields.io/badge/MAVLink-2.0-red.svg)](https://mavlink.io)

**Phase 3**: Evolution into an intelligent agentic architecture enabling end-to-end automation and integration with enterprise systems.

In this phase, Aero Companion transitions from manual or pre-scripted operation to an intelligent, event-driven system where autonomous agents manage mission workflows based on real-world triggers. The drone system becomes deeply integrated with customer operations, logistics systems, and edge/cloud-based agents that drive mission planning, coordination, and oversight.

# n8n Workflow Integration

Using n8n these integrations transform your autonomous drone into a complete business solution that seamlessly connects with existing enterprise systems.

## Real-Time Alert & Response Workflows

### Security Monitoring Pipeline
Transform your drone into an intelligent security system that automatically responds to threats:

- **Instant Threat Detection**: Computer vision module feeds directly into n8n workflows
- **Multi-Channel Alerting**: Automatic SMS, email, and Slack notifications when unauthorized personnel detected
- **Smart Escalation**: Threat severity assessment triggers appropriate response levels
- **Enterprise Integration**: Direct integration with security management systems and CRM platforms
- **Evidence Collection**: Automatic screenshot capture and GPS coordinate logging

```json
{
  "workflow": "security_alert",
  "trigger": "cv_detection",
  "actions": ["sms_alert", "slack_notification", "video_capture", "gps_log"]
}
```

### Environmental Monitoring Chain
Deploy for environmental compliance and emergency response:

- **Anomaly Detection**: Real-time monitoring for oil spills, fires, flooding, or chemical leaks
- **Authority Notification**: Automatic alerts to EPA, fire departments, or emergency services
- **Work Order Generation**: Direct integration with maintenance management systems
- **Regulatory Reporting**: Automated compliance documentation and incident reports
- **Multi-Site Coordination**: Orchestrate response across multiple drone deployments

## Automated Mission Triggering & Agentic Workflows

### Autonomous Delivery Dispatch
Transform e-commerce and logistics operations with fully automated drone deployment:

**End-to-End Automation Example:**
1. **Order Detection**: Customer places order in e-commerce system
2. **Intelligent Agent Processing**: n8n agent intercepts order event and extracts delivery parameters
3. **Drone Selection**: Algorithm identifies optimal available drone based on location
4. **Mission Generation**: Automatically creates JSON mission profile from order details
5. **Remote Deployment**: Mission file deployed to drone's USB drive via secure remote access
6. **Human Coordination**: Automated notifications to warehouse staff for payload loading
7. **Autonomous Launch**: Drone executes delivery using computer vision and GPS/SLAM navigation upon battery connection

```json
{
  "delivery_mission": {
    "order_id": "ORD-2024-001",
    "destination": {"lat": 40.7128, "lng": -74.0060},
    "payload": {"weight": 0.5, "dimensions": "10x10x5"},
    "delivery_window": "2024-07-24T14:00:00Z",
    "drone_id": "AC-001",
    "priority": "standard"
  }
}
```

### Intelligent Agent Responsibilities

**Mission Generation Engine**
- **Event Translation**: Convert business events (orders, inspections, emergencies) into executable drone missions
- **Parameter Optimization**: Intelligent route planning considering weather, airspace, and efficiency
- **Mission Validation**: Automatic verification of mission feasibility and safety parameters

**Inventory & Resource Coordination**
- **Fleet Management**: Real-time tracking of drone availability, battery levels, and maintenance status
- **Proximity Matching**: Optimize drone selection based on geographic location and mission requirements
- **Load Balancing**: Distribute missions across available drones to maximize fleet utilization

**Human-In-The-Loop Orchestration**
- **Task Assignment**: Automated notifications to appropriate personnel for physical tasks
- **Workflow Coordination**: Synchronize human activities with autonomous operations
- **Progress Tracking**: Monitor completion of manual tasks and trigger next automation steps
- **Escalation Management**: Route issues to appropriate personnel based on urgency and expertise

**Comprehensive Audit & Compliance**
- **Full Mission Logging**: Complete audit trail from order receipt to delivery confirmation
- **Regulatory Compliance**: Automatic generation of required aviation and commercial documentation
- **Cost Tracking**: Real-time calculation of operational costs and profitability per mission

**Dynamic Mission Management**
- **Real-Time Monitoring**: Continuous tracking of flight progress and mission status
- **Stakeholder Updates**: Automated notifications to customers, dispatchers, and management
- **Route Optimization**: Dynamic path adjustment based on weather, traffic, and obstacles
- **Delivery Confirmation**: Automated proof-of-delivery with photo/video evidence

**Intelligent Incident Response**
- **Safety Event Detection**: Automatic recognition of geofence breaches, low battery, or SLAM failures
- **Escalation Protocols**: Smart routing of incidents based on severity and required response
- **Emergency Procedures**: Automated execution of safety protocols including emergency RTL
- **Recovery Coordination**: Orchestration of drone recovery and mission continuation procedures
