$(document).ready(function () {
    $("INPUT#btn_translate").click(function (e) { 
        e.preventDefault();
        let lang = $('INPUT#language_code').val();
        $.ajax({
            type: "GET",
            url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
            success: function (response) {
                $('DIV#hello').text(response.hello);
                $('INPUT#language_code').val('');
            }
        });
    });
});