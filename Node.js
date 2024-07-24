const dgram = require('dgram');
const server = dgram.createSocket('udp4');

server.on('message', (msg, rinfo) => {
    console.log(`Server got: ${msg} from ${rinfo.address}:${rinfo.port}`);
    // Decrypt and verify the message here
});

server.bind(41234, () => {
    console.log('UDP server is listening on port 41234');
});
