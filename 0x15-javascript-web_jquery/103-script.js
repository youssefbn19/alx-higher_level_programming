$(document).ready(function () {
    $("INPUT#btn_translate").click(function (e) { 
        e.preventDefault();
        let lang = $('INPUT#language_code').val();
        helloDefLang(lang);
    });
    $('INPUT#language_code').keypress(function (e) { 
        if (e.which == 13)
        {
            let lang = $('INPUT#language_code').val();
            helloDefLang(lang);
        }
    });
});
function helloDefLang(lang){
    $.ajax({
        type: "GET",
        url: `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
        success: function (response) {
            $('DIV#hello').text(response.hello);
            $('INPUT#language_code').val('');
        }
    });
}