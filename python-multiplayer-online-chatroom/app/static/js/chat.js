$(document).ready(function () {
    // Define a persistent connection
    var conn = null;

    // Get client's name and avatar
    var name = $("#input_name").val();
    var avatar = $("#input_avatar").val();

    // Define connection
    function connect() {
        // disconnect if connected
        disconnect();

        var transports = ["websocket", "xhr-streaming", "iframe-eventsource", "iframe-htmlfile", "xhr-polling", "iframe-xhr-polling", "jsonp-polling"];

        conn = new SockJS("http://" + window.location.host + "/chatroom", transports);

        // client initiates a connection
        conn.onopen = function () {

        };

        // full duplex communication
        conn.onmessage = function (e) {
            console.log(e);
        };

        // close the connection
        conn.onclose = function (e) {
            conn = null;
        };
    }


    // Disconnect
    function disconnect() {
        if (conn != null) {
            conn.close();
            conn = null;
        }
    }


    if (conn == null) {
        connect();
    } else {
        disconnect();
    }


    function getFormData() {
        var arr = $("#form-data").serializeArray();
        var obj = {};
        $.map(arr, function (n, i) {
            obj[n['name']] = n['value'];
        });
        return obj
    }

    $("send_msg").click( function () {
        var msg_data = getFormData();
        console.log("msg_data below")
        console.log(msg_data)
        console.log("msg_data.content below")
        console.log(msg_data.content)
        if (msg_data.content) {
            msg_data.code = 2;
            ue.setContent('');
            conn.send(JSON.stringify(msg_data));
        } else {
            alert("Can't send out an empty message.");
        }
    });



});
