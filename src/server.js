const WebSocket = require('ws');
const dgram = require('dgram');
const fs = require('fs');
const path = require('path');
const udpServer = dgram.createSocket('udp4');
const wss = new WebSocket.Server({ port: 8080 });

// Ensure log directory exists
const logDir = path.join(__dirname, 'logs');
if (!fs.existsSync(logDir)) {
  fs.mkdirSync(logDir);
}

wss.on('connection', ws => {
  console.log('Connected');
  ws.on('message', message => {
    console.log(`message: ${message}`);
    logMessageToFile(message);
    wss.clients.forEach(client => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  });

  ws.on('close', () => {
    console.log('disconnected');
  });
});

udpServer.on('message', (msg, rinfo) => {
  console.log(`UDP message from ${rinfo.address}:${rinfo.port}: ${msg}`);
  logMessageToFile(msg.toString());
  broadcastMessage(msg.toString());
});

udpServer.on('listening', () => {
  const address = udpServer.address();
  console.log(`UDP server listening at ${address.address}:${address.port}`);
});

udpServer.bind(41234);

function logMessageToFile(message) {
  const date = new Date().toISOString().split('T')[0];
  const filename = path.join(logDir, `log_${date}.json`);

  const logEntry = {
    timestamp: new Date().toISOString(),
    message
  };

  fs.appendFile(filename, JSON.stringify(logEntry) + '\n', err => {
    if (err) {
      console.error('Error writing to log file', err);
    }
  });
}

function broadcastMessage(message) {
  wss.clients.forEach(client => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(message);
    }
  });
}
