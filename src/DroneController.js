import React, { useState, useEffect, useRef } from 'react';
import { Joystick } from 'react-joystick-component';
import CryptoJS from 'crypto-js';

const DroneController = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [loginKey, setLoginKey] = useState('');
  const [commandInput, setCommandInput] = useState('');
  const secureKey = 'key'; // Replace with your actual secure key
  const commandInputRef = useRef(null);
  const recordButtonRef = useRef(null);
  const streamButtonRef = useRef(null);
  const recognitionRef = useRef(null); 
  const [lastCommand, setLastCommand] = useState('');
  const wsRef = useRef(null);

  useEffect(() => {
    document.addEventListener('gesturestart', function (e) {
      e.preventDefault();
    });
    document.addEventListener('gesturechange', function (e) {
      e.preventDefault();
    });
    document.addEventListener('gestureend', function (e) {
      e.preventDefault();
    });

    // Initialize WebSocket connection
    wsRef.current = new WebSocket('ws://10.0.0.186:8080');

    // Initialize speech recognition
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (SpeechRecognition) {
      const recognition = new SpeechRecognition();
      recognition.continuous = true;
      recognition.interimResults = false;
      recognition.lang = 'en-US';
      recognition.onresult = (event) => {
        const command = event.results[event.results.length - 1][0].transcript.trim().toUpperCase();
        processVoiceCommand(command);
      };
      recognitionRef.current = recognition;
    } else {
      alert('Speech Recognition API not supported in this browser.');
    }

    return () => {
      if (wsRef.current) {
        wsRef.current.close();
      }
    };
  }, []);

  const handleLogin = () => {
    if (loginKey === secureKey) {
      setIsLoggedIn(true);
    } else {
      alert('Incorrect key. Please try again.');
    }
  };

  const handleCommand = (command) => {
    //if (command !== lastCommand) {
      appendCommand(command);
      sendUdpCommand(command);
      setLastCommand(command);
    //}
  };

  const appendCommand = (command) => {
    setCommandInput((prev) => `${prev}${command}\n`);
    if (commandInputRef.current) {
      commandInputRef.current.scrollTop = commandInputRef.current.scrollHeight;
    }
  };

  const encryptMessage = (message, key) => {
    const iv = CryptoJS.lib.WordArray.random(16);
    const encrypted = CryptoJS.AES.encrypt(message, key, { iv: iv });
    return iv.concat(encrypted.ciphertext).toString(CryptoJS.enc.Base64);
  };

  const hmacHash = (message, key) => {
    return CryptoJS.HmacSHA256(message, key).toString();
  };

  const sendUdpCommand = (command) => {
    const key = CryptoJS.enc.Hex.parse(secureKey);
    const timestamp = Date.now().toString();
    const nonce = CryptoJS.lib.WordArray.random(16).toString();
    const message = `${command}|${timestamp}|${nonce}`;
    const encryptedMessage = encryptMessage(message, key);
    const hash = hmacHash(encryptedMessage, key);
    const udpMessage = `${encryptedMessage}|${hash}`;

    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
        console.log('Sending command:', udpMessage);
        wsRef.current.send(udpMessage);
      } else {
        //reconnect and retry
        wsRef.current = new WebSocket('ws://10.0.0.186:41234');
        wsRef.current.send(udpMessage);
      }
  };

  const handleRecordButtonClick = () => {
    const recordButton = recordButtonRef.current;
    if (recordButton) {
      const isRecording = recordButton.classList.toggle('record-on');
      recordButton.style.backgroundColor = isRecording ? 'red' : 'grey';
      handleCommand(isRecording ? 'Voice Record On' : 'Voice Record Off');
      
      if (isRecording && recognitionRef.current) {
        recognitionRef.current.start();
      } else if (recognitionRef.current) {
        recognitionRef.current.stop();
      }

      navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
        const audioTracks = stream.getAudioTracks();
        audioTracks.forEach(track => track.stop());
      });
    }
  };

  const handleStreamButtonClick = () => {
    const streamButton = streamButtonRef.current;
    if (streamButton) {
      const isStreaming = streamButton.classList.toggle('stream-on');
      streamButton.style.backgroundColor = isStreaming ? 'blue' : 'grey';
      handleCommand(isStreaming ? 'Video Stream On' : 'Video Stream Off');
    }
  };

  const restrictJoystickMovement = (data, joystick) => {
    let commandString = '';
  
    if (joystick === 'left') {
      if (data.direction) {
        if (data.direction === 'FORWARD') {
          commandString = 'Move Up';
        } else if (data.direction === 'LEFT') {
          commandString = 'Pan Left';
        } else if (data.direction === 'BACKWARD') {
          commandString = 'Move Down';
        } else if (data.direction === 'RIGHT') {
          commandString = 'Pan Right';
        }
      }
    } else if (joystick === 'right') {
      if (data.direction) {
        if (data.direction === 'FORWARD') {
          commandString = 'Move Forward';
        } else if (data.direction === 'LEFT') {
          commandString = 'Roll Left';
        } else if (data.direction === 'BACKWARD') {
          commandString = 'Move Backward';
        } else if (data.direction === 'RIGHT') {
          commandString = 'Roll Right';
        }
      }
    }
    if (commandString) {
      handleCommand(commandString);
    }
  };

  const processVoiceCommand = (command) => {
    const voiceCommands = {
      'MOVE UP': 'Move Up',
      'PAN LEFT': 'Pan Left',
      'MOVE DOWN': 'Move Down',
      'PAN RIGHT': 'Pan Right',
      'MOVE FORWARD': 'Move Forward',
      'ROLL LEFT': 'Roll Left',
      'MOVE BACKWARD': 'Move Backward',
      'ROLL RIGHT': 'Roll Right'
    };

    if (voiceCommands[command]) {
      handleCommand(voiceCommands[command]);
    }
  };

  return (
    <div style={{ height: '100vh', width: '100vw', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', backgroundColor: '#333' }}>
      {!isLoggedIn ? (
        <div style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', background: 'rgba(0, 0, 0, 0.8)', zIndex: 3 }}>
          <input type="password" placeholder="Enter your key" value={loginKey} onChange={(e) => setLoginKey(e.target.value)} style={{ padding: '10px', marginBottom: '10px', border: '1px solid #ccc', borderRadius: '5px', fontSize: '16px' }} />
          <button onClick={handleLogin} style={{ padding: '10px 20px', border: 'none', borderRadius: '5px', background: '#555', color: 'white', fontSize: '16px', cursor: 'pointer', transition: 'background-color 0.3s' }}>
            Login
          </button>
        </div>
      ) : (
        <>
          <div style={{ flexGrow: 1, position: 'relative', width: '100%', height: '100%' }}>
            <video id="drone-video" width="100%" height="100%" autoPlay style={{ objectFit: 'cover' }}></video>
            <div id="no-signal" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', position: 'absolute', top: '50%', left: '50%', transform: 'translate(-50%, -50%)', color: 'white', background: 'rgba(0, 0, 0, 0.75)', padding: '10px 20px', fontSize: '20px', borderRadius: '5px', zIndex: 2 }}>
              No Signal
            </div>
          </div>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '20px', position: 'fixed', bottom: 0, left: 0, right: 0, marginBottom: '20px', gap: '10px' }}>
            <Joystick size={100} baseColor="gray" stickColor="red" move={(e) => restrictJoystickMovement(e, 'left')} />
            <button
              id="record-button"
              ref={recordButtonRef}
              className="record-off"
              onClick={handleRecordButtonClick}
              style={{ width: '50px', height: '50px', backgroundColor: 'grey', borderRadius: '50%', border: 'none', cursor: 'pointer', transition: 'background-color 0.3s', margin: '0 10px' }}
            />
            <textarea
              ref={commandInputRef}
              value={commandInput}
              placeholder="Command output"
              readOnly
              style={{ flexGrow: 1, padding: '10px', background: 'white', border: '1px solid #ccc', borderRadius: '5px', textAlign: 'center', margin: '0 10px', height: '25px', overflowY: 'scroll' }}
            />
            <button
              id="stream-toggle"
              ref={streamButtonRef}
              className="stream-off"
              onClick={handleStreamButtonClick}
              style={{ width: '50px', height: '50px', backgroundColor: 'grey', borderRadius: '50%', border: 'none', cursor: 'pointer', transition: 'background-color 0.3s', margin: '0 10px' }}
            />
            <Joystick size={100} baseColor="gray" stickColor="blue" move={(e) => restrictJoystickMovement(e, 'right')} />
          </div>
        </>
      )}
    </div>
  );
};

export default DroneController;
