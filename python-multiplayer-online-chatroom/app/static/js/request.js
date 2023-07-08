/*
* clients send requests to the server，based on http protocol，ajax
* url：请求地址
* rurl：跳转地址
* fields：验证字段
* msg：消息提示
* */
function request(url, rurl, fields, msg) {
    $("#btn-sub").click(function () {
        console.log("Button is clicked")
        var data = $("#form-data").serialize();
        console.log("form-data sent by request")
        console.log(data)
        $.ajax({
            url: url,
            data: data,
            dataType: "json",
            type: "POST",
            success: function (res) {
                // If request successful, code = 1
                if (res.code == 1) {
                    console.log("Request is successful.")
                    alert(msg);
                    location.href = rurl;
                } else {
                    console.log("Request failed.")
                    for (var k in fields) {
                        if (typeof res[fields[k]] == "undefined") {
                            $("#error-" + fields[k]).empty();
                        } else {
                            $("#error-" + fields[k]).empty();
                            $("#error-" + fields[k]).append(
                                res[fields[k]]
                            );
                        }
                    }
                }
            }
        });
    });
}