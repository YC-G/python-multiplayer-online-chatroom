/*
    k, name, avatar
    w, width, 200
    h, height, 200
    url, address
*/
function upload(k, w, h, url) {
    $("#upload_"+k).click(function() {
        var img = $("#file_"+k)[0].files[0];
        if(img){
            var formData = new FormData();
            formData.append("img", img);
            $.ajax({
                url: url,
                type: "POST",
                dataType: "json",
                data: formData,
                cache: false,
                contentType: false,
                processData: false,
                success: function(res) {
                    if (res.code == 1) {
                        var image = res.image;
                        var content = "<img src='/static/uploads/" + image + "' style='width: 200px;200px;'>";
                        $("#image_"+k).empty();
                        $("#image_"+k).append(content);
                        $("#input_"+k).attr("value", image)
                    }
                }

            });
        }
    });
}