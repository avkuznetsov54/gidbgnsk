$(document).ready(function() {

  $('.js-example-basic-single').select2();
  $('.js-example-basic-multiple').select2();

  $('.search-multiple.js-example-basic-multiple').select2({
        placeholder: "Выберите",
        minimumResultsForSearch: 5
    });

  $('#example-multiple-optgroups').multiselect({
        	enableClickableOptGroups: true,
            enableCollapsibleOptGroups: true,
            // enableFiltering: true,
            includeSelectAllOption: true
        });
  $('.boo-multi').multiselect({
            Placeholder: 'Search for something...',
        	enableClickableOptGroups: true,
            enableCollapsibleOptGroups: true,
            // enableFiltering: true,
            includeSelectAllOption: true
        });




  // search
  $('.panel-main2').on('change', '.search-panel2', function (e) {
    e.preventDefault();

    // забираем все выбранные чекбоксы
    var checkValues = $('input[name=horns]:checked').map(function(){
        return $(this).val();
    }).get();

    // забираем значения выбранные селектом
    var jkValues = $('select[name=jkobject]').val();
    var cbValues = $('select[name=classbuilding]').val();


    // var jkValues2 = $('select[name=jkobject]').find(':selected').data();
    // var cbValues2 = $('select[name=classbuilding]').find(':selected').data('param');
    //
    // var jkValues2 = $('select[name=jkobject]').map(function(){
    //     return $(this).data();
    // });

    // multi values, with last selected
    // var old_values = [];
    // $('select[name=jkobject]').on('select2:select', function (e) {
    //     let id = $(e.params.data.element).data('param');
    //     let vl = $(e.params.data)[0].text;
    //     if (id == 'class'){
    //       console.log('привет')
    //       console.log(vl)
    //     }else {
    //       console.log('нет')
    //     }

      // var values = [];
      // // copy all option values from selected
      // $(e.currentTarget).find("option:selected").each(function(i, selected){
      //   values[i] = $(selected).text();
      //   // console.log(values)
      // });
      // // doing a diff of old_values gives the new values selected
      // var last = $(values).not(old_values).get();
      // // update old_values for future use
      // old_values = values;
      // // output values (all current values selected)
      // // console.log("selected values: ", values);
      // // output last added value
      // console.log("last added: ", last);
    // });


    var form = $(this);
    var formData = new FormData(this);
    $.ajax({
      url: form.attr('data-url'),
      type: 'POST',
      data: formData,
      dataType: 'json',
      cache: false,
      contentType: false,
      processData: false,
      beforeSend: function () {
        formData.set('horns', checkValues);
        formData.set('jkobject', jkValues);
        formData.set('classbuilding', cbValues);
      },
      success: function (data) {
        if(data.is_valid){
          console.log(data);
          // $('.ajax-list-card').remove();
          $('.ajax-list-card').html(data.html);
          // $('.get-list-card').remove();

          // form.find('.wr-form').attr('style', 'display:none;');
          // form.find('.response-form').html(data.message);
          // form.find('.anim-process-send').attr('style', 'display:none;'); // отключим
          // form.find('.anim-process-done').attr('style', '');

        } else {
          // $('.modal-notice .modal-content').html(data.html_form);
          // // form.find('.wr-form').attr('style', 'display:none;');
          // // form.find('.response-form').html(data.message);
        }
      },
      error: function (xhr, ajaxOptions, thrownError) {
        console.log(arguments);
        console.log('не передалось AJAX');
        console.log(formData);
      }
    })
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