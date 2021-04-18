$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $('.tabs').tabs();
    });

$(function(){
    new NiceCountryInput($(".countrypicker")).init();
});

function onChangeCallback(ctr){
  console.log("The country was changed: " + ctr);
}