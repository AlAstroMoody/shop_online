(function ($) {
    $(function () {

        $('.sidenav').sidenav();
        $('.parallax').parallax();
        $(".dropdown-trigger").dropdown();

        (function quantityProducts() {
            let $quantityArrowMinus = $(".quantity-arrow-minus");
            let $quantityArrowPlus = $(".quantity-arrow-plus");
            let $quantityNum = $(".quantity-num");
            let $newPrice = $(".new-price");
            let submit_btn = $(".submit_btn");
            let product_id = submit_btn.data('product_id')
            let product_name = submit_btn.data('product_name')
            let product_price = submit_btn.data('product_price')

            $quantityArrowMinus.click(quantityMinus);
            $quantityArrowPlus.click(quantityPlus);

            function quantityMinus() {
                if ($quantityNum.val() > 1) {
                    $quantityNum.val(+$quantityNum.val() - 1);
                    $newPrice.val(product_price * +$quantityNum.val());
                }
            }

            function quantityPlus() {
                $quantityNum.val(+$quantityNum.val() + 1);
                $newPrice.val(product_price * +$quantityNum.val());
            }

        })();
    }); // end of document ready
})(jQuery); // end of jQuery name space

$(document).ready(function () {
    $('ul.tabs').tabs();
    $('.materialboxed').materialbox();
    $('.tooltipped').tooltip();
    $('.card').mouseover(function () {
        $('.card-detail').toggleClass('hidden')
    });

});

