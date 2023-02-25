#!/usr/bin/env node

const websocket = new WebSocket('ws://localhost:8001/')

websocket.addEventListener('message', (event) => {
    console.log('Message from server', event.data);
});


