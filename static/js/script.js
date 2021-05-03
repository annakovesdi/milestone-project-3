$(document).ready(function () {
    $(".sidenav").sidenav({ edge: "right" });
    $('.tabs').tabs();
});

function onChangeCallback(ctr) {
    console.log("The country was changed: " + ctr);
}