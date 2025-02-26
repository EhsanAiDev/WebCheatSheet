// handeling data from server and clinet 

const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/SOME_FUCKING_PATH/'
);


// when data resive from server
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data.message);
};


// sending data to server 
function sendMessage(message) {
    const data = JSON.stringify({"message" : message})
    chatSocket.send(data);
}


// when connection lost 
chatSocket.onclose = function(e) {
  console.error('Chat socket closed unexpectedly');
};


