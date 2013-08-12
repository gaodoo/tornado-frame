$(function(){
    $('#login-show').click(function(){
        $('#login-form').show().siblings('#register-form').hide();
    })
    $('#register-show').click(function(){
        $('#register-form').show().siblings('#login-form').hide();
    })
})
