$(function() {
  $('#submit').click(function() {
    event.preventDefault();
    var form_data = new FormData($('#uploadform')[0]);
    $.ajax({
      type: "POST",
      url: '/',
      data: form_data,
      contentType: false,
      processData: false,
      dataType: false,

    });
    $.ajax({
      type: 'POST',
      url: '/uploadajax',
      data: form_data,
      contentType: false,
      processData: false,
      dataType: false
    }).done(function(data, textStatus, jqXHR) {
      console.log(data);
      console.log(textStatus);
      console.log(jqXHR);
      console.log('Success!');
      var name;
      $("#resultFilename").text(data['name']);
      $("#resultFilesize").text(data['size']);
      if (typeof data['name'] === "string") {
        var ary = data['name'].split('.');
        if (ary.length > 2) {
          name = data['name'].replace("." + data[data.length - 1], "");

        } else {
          name = ary[0];
        }
      }
      $("#resImg").attr({
        src: "static/cBgImg/" + name + ".png",
        title: false,
        alt: false
      });
    }).fail(function(data) {
      alert('error!');
    });
  });
});
