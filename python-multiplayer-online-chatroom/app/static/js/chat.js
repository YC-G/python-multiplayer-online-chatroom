$(document).ready(function () {
    //1.定义长连接
    var conn = null;
    //2.获取昵称，头像
    var name = $("#input_name").val();
    var face = $("#input_face").val();

    // 追加聊天消息框
    function append_msg(name, data) {
        var html = "";
        if (data.code == 2) {
            if (name == data.name) {
                //代表我自己
                html += "<div class=\"row\">";
                html += "<div class=\"col-md-3\"></div>";
                html += "<div class=\"col-md-9\">";
                html += "<div class=\"media\">";
                html += "<div class=\"media-body\">";
                html += "<h6 class=\"user-nickname text-right\">" + data.name + "[" + data.dt + "]</h6>";
                html += "<div class=\"alert alert-success\" role=\"alert\">";
                html += data.content;
                html += "</div>";
                html += "</div>";
                html += "<img class=\"ml-3 rounded-circle\" style='width: 60px;height: 60px;' src=\"" + data.face + "\">";
                html += "</div></div></div>";
            } else {
                html += "<div class=\"row\">";
                html += "<div class=\"col-md-9\">";
                html += "<div class=\"media\">";
                html += "<img class=\"mr-3 rounded-circle\" style='width: 60px;height: 60px;' src=\"" + data.face + "\">";
                html += "<div class=\"media-body\">";
                html += "<h6 class=\"user-nickname\">" + data.name + "[" + data.dt + "]</h6>";
                html += "<div class=\"alert alert-info\" role=\"alert\">";
                html += data.content;
                html += "</div>";
                html += "</div>";
                html += "</div></div>";
                html += "<div class=\"col-md-3\"></div>";
                html += "</div>";
            }
        } else if (data.code == 1) {
            html += "<p class='text-center text-success'>欢迎" + data.name + "进入聊天室！<img src='/static/images/rorse.gif'><img src='/static/images/rorse.gif'><img src='/static/images/rorse.gif'></p>"
        }
        $("#chat-list").append(html);
        SyntaxHighlighter.highlight();
        $("#chat-list").scrollTop($("#chat-list").scrollTop() + 9999999);
    }

    // 更新UI函数
    function update_ui(event) {
        var data = event.data;
        data = JSON.parse(data);
        append_msg(name, data);
    }

    //3.定义连接
    function connect() {
        //之前连接没有断开先将其断开
        disconnect();
        var transports = [
            "websocket", "xhr-streaming",
            "iframe-eventsoure", "iframe-htmlfile",
            "xhr-polling", "iframe-xhr-polling",
            "jsonp-polling"
        ];
        conn = new SockJS("http://" + window.location.host + "/chatroom", transports);
        //客户端发起连接
        conn.onopen = function () {
            $.ajax({
                url: "/msg/",
                type: "POST",
                dataType: "json",
                success: function (res) {
                    var msg_data = res.data;
                    for (var k in msg_data) {
                        append_msg(name, msg_data[k]);
                    }
                    var enter_data = {
                        code: 1,
                        name: name,
                        face: face
                    };
                    conn.send(JSON.stringify(enter_data));
                }
            });

        };
        //双向通信
        conn.onmessage = function (event) {
            //console.log(e);
            update_ui(event);
        };
        //关闭连接
        conn.onclose = function () {
            conn = null;
        }
    }

    //4.断开连接
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

    // 获取表单数据
    function getFormData() {
        var arr = $("#form-data").serializeArray();
        var obj = {};
        $.map(arr, function (n, i) {
            obj[n['name']] = n['value'];
        });
        return obj
    }

    $("#send_msg").click(function () {
        var msg_data = getFormData();
        if (msg_data.content) {
            msg_data.code = 2;
            ue.setContent('');
            console.log(msg_data);
            conn.send(JSON.stringify(msg_data));
        } else {
            alert("发送消息不能为空！");
        }
    });
});