(function ($) {
    $(function () {

        $('.sidenav').sidenav();
        $('.parallax').parallax();

        $(".dropdown-trigger").dropdown();

    }); // end of document ready
})(jQuery); // end of jQuery name space
$(document).ready(function(){
  $('ul.tabs').tabs();
});
$(document).ready(function(){
  $('ul.tabs').tabs('select_tab', 'tab_id');
});