const home = document.querySelector('.home-page')
const contribute = document.querySelector('.contribute-page')
const search = document.querySelector('.search-page')
const url = window.location.pathname

if (url.endsWith('search')) {
    search.classList.add('active');
    contribute.classList.remove('active');
    home.classList.remove('active');
}

if (url.endsWith('home')) {
    home.classList.add('active');
    contribute.classList.remove('active');
    search.classList.remove('active');
}

if (url.endsWith('contribute')) {
    contribute.classList.add('active');
    search.classList.remove('active');
    home.classList.remove('active');
}

function progress() {
    $('#upload').submit(function(event){
        if($('#file-upload').val()){
            event.preventDefault();
            $('#target_layer').hide();
            $(this).ajaxSubmit({
                target: '#target_layer',
                beforeSubmit:function(){
                    $('.progress-bar').width('50%');
                },
                uploadProgress: function(event, position, total, percentageComplete)
                {
                    $('.progress-bar').animate({
                        width: percentageComplete + '%'
                    }, {
                        duration: 1000
                    });
                },
                success:function(data){
                    $('#target_layer').show();
                    $('#target_layer').append(data.htmlresponse);
                },
                resetForm: true
            });
        }
        return false;
    });
}

$(document).ready(progress());

// function loadmore() {
//     $(".grid").slice(0,18).show();
//     $("#loadmore").click(function(event){
//         event.preventDefault();
//         $(".grid:hidden").slice(0,12).slideDown();
//         if($(".grid:hidden").length == 0) {
//             $("#loadmore").text("No More Images").addClass("noContent");
//         }
//     });
// };

// $(document).ready(loadmore());