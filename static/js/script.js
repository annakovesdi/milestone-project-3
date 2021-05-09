$(document).ready(function () {
    $(".sidenav").sidenav({ edge: "right" });
    $('.tabs').tabs();
    $('.modal').modal();
    $('.trigger-modal').modal();
});

function onChangeCallback(ctr) {
    console.log("The country was changed: " + ctr);
}