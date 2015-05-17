function checkUser() {
    username = $("#id_username").val();
    console.log("Username ", username);
    $.ajax({
        "url": "/checkuser",
        "data": {
            "username": username
        }
    }).done(function(data){
        $(".usererr").remove();
        if(data === 'taken'){
            html = "<div class=\"usererr err\">username is already taken</div>";
            $("body > form > p:nth-child(2)").append(html);


        }
        console.log(data);
    })
}



function validateEmail() {
    email = $("#id_email").val();
    if (email == "") {
        return false;
    }
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return re.test(email);
}

function validatePassword() {
    pass1 = $("#id_password1").val();
    pass2 = $("#id_password2").val();
    if(pass2 ==="")
        return false;
    else return pass1 === pass2;
}

$(function() {
    $("#id_username").blur(function() {
        checkUser();
    });
    $("#id_email").blur(function() {
        $(".emailerr").remove();
        if (!validateEmail()) {
            html = "<div class=\"emailerr err\">Please enter valid email</div>";
            $("body > form > p:nth-child(3)").append(html);
        }
    });

    $("#id_password2").blur(function() {
        $(".passerr").remove();
        if(!validatePassword()) {
            html = "<div class=\"passerr err\">password not match </div>";
            $("body > form > p:nth-child(5)").append(html);
        }
    });
});
