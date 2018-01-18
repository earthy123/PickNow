$(function() {
    $('#submit').click(function() {
        event.preventDefault();
        var form_data = new FormData($('#uploadform')[0]);
        console.log('form_data',form_data);
        $.ajax({
            type: 'POST',
            url: '/',
            data: form_data,
            contentType: false,
            processData: false,
            dataType: 'json'
        }).done(function(data, textStatus, jqXHR){
            console.log('data',data);
            console.log(textStatus);
            console.log(jqXHR);
            console.log('Success!');
            $("#resultFilename").text(data['name']);
            $("#resultFilesize").text(data['size']);
            $("#resImg").attr({
              src: "/static/cBgImg/hallo.png",
              title: "jQuery",
              alt: "jQuery Logo"
            });
        }).fail(function(data){
          console.error('error',data);
            alert('error!');
        });
    });
});
