$(document).ready(function() {

  $('.js-example-basic-single').select2();
  $('.js-example-basic-multiple').select2();

  $('.search-multiple.js-example-basic-multiple').select2({
        placeholder: "Выберите",
        minimumResultsForSearch: 5
    });



  // чтобы форма отобразилась
  $('.show-form').click(function () {
    var butt = $(this);
    $.ajax({
      url: '/notice/create/',
      type: 'get',
      data: {
        'data-notice-name': butt.attr('data-notice-name'),
        'data-object-name': butt.attr('data-object-name'),
        'data-obj-dev-name': butt.attr('data-obj-dev-name')
      },
      dataType: 'json',
      beforeSend: function () {
        // $('.modal-notice').modal('show');
      },
      success: function (data) {
        $('.modal-notice .modal-content').html(data.html_form);
      }
    })
  });

  // отправка формы
  $('.modal-notice').on('submit', '.create-form', function () {
    var form = $(this);
    var formData = new FormData(this);
    $.ajax({
      url: form.attr('data-url'),
      // data: form.serialize(),
      data: formData,
      type: form.attr('method'),
      dataType: 'json',
      cache: false,
      contentType: false,
      processData: false,
      beforeSend: function () {
        form.find('button').attr('disabled', true); // отключим кнопку
        form.find('.wr-form').attr('style', 'display:none;');
        form.find('.anim-process-send').attr('style', ''); // включаем
      },
      success: function (data) {
        if(data.form_is_valid){
          console.log('data is save')
          form.find('.wr-form').attr('style', 'display:none;');
          form.find('.response-form').html(data.message);
          form.find('.anim-process-send').attr('style', 'display:none;'); // отключим
          form.find('.anim-process-done').attr('style', '');

        } else {
          $('.modal-notice .modal-content').html(data.html_form);
          // form.find('.wr-form').attr('style', 'display:none;');
          // form.find('.response-form').html(data.message);
        }
      },
      complete: function() { // в конце любого исхода
							form.find('button').prop('disabled', false); // снова включим кнопку
					}
    });
    return false;
  });


});