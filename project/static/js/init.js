(function ($) {
    $(function () {
        $('.sidenav').sidenav();
        $('.parallax').parallax();
        $(".dropdown-trigger").dropdown();

    });
})(jQuery);

$(document).ready(function () {
    $('ul.tabs').tabs();
    $('.materialboxed').materialbox();
    $('.tooltipped').tooltip();
    $('.card').mouseover(function () {
        $('.card-detail').toggleClass('hidden')
    });

    (function quantityProducts() {
        let $quantityArrowMinus = $(".quantity-arrow-minus");
        let $quantityArrowPlus = $(".quantity-arrow-plus");
        let $quantityNum = $(".quantity-num");
        let $newPrice = $(".new-price");
        let submit_btn = $(".submit_btn");
        let product_price = submit_btn.data('product_price')
        let product_id = submit_btn.data('product_id');
        let product_name = submit_btn.data('product_name');
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

        let form = $('#form_buying_product');
        form.on('submit', function (e) {
            e.preventDefault();
            console.log(product_id)
            basketUpdating(product_id, $quantityNum.val(), is_delete = false)
        });

        function basketUpdating(product_id, quantityNum, is_delete) {
            let data = {};
            data.product_id = product_id;
            data.quantityNum = quantityNum;
            let csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
            data["csrfmiddlewaretoken"] = csrf_token;
            if (is_delete) {
                data["is_delete"] = true;
            }
            let url = form.attr("action");

            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                success: function (data) {
                    if (!data.is_anonymous) {
                        if (data.total_quantity) {
                            $('#total_quantity').text(data.total_quantity + '(' + data.sum_quantity + ')')
                        }
                        if (data.total_quantity || data.total_quantity === 0) {
                            $('#total_quantity').text(data.total_quantity + '(' + data.sum_quantity + ')');
                            $('.basket-items ul').html("");
                        }
                    }
                },
                failure: function (data) {
                    console.log('Error AJAX');
                }
            });
        }

        $(document).on('click', '.delete-item', function (e) {
            e.preventDefault()
            product_id = $(this).data("product_id")
            $(this).closest('tr').remove()
            let quantityNum = 0
            basketUpdating(product_id, quantityNum, is_delete = true)
        })
    })();
});
