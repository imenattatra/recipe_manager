$(document).ready(function () {
    /***
    Scipt for toggle sidebar
    ***/
        $('#sidebarCollapse').on('click', function () {
            $('#sidebar').toggleClass('active');
        });
   
    /***
    Scipt for confirm delete
    ***/
    $(".delete-ingredient").on('click', function (e) {
        e.preventDefault();
        const url = $(this).attr("href");
        const deleteForm = $("#object_delete_form");
        deleteForm.attr("action", url);
        deleteForm.find("#object_delete_name", $(this).attr("id"));
        const modal = $("#delete-modal").modal('show');
    });
    $(".delete-recipe").on('click', function (e) {
        e.preventDefault();
        const url = $(this).attr("href");
        const deleteForm = $("#object_delete_form");
        deleteForm.attr("action", url);
        deleteForm.find("#object_delete_name", $(this).attr("id"));
        const modal = $("#delete-modal").modal('show');
    });

    /***
    Scipt to display image preview when adding an image in a form
    ***/
    
    $('#image').click(function(){
        $('#myfile').click();
    });
    $('#myfile').change(function(){
        readURL(this);
    });
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            
            reader.onload = function(e) {
            $('#element_image').attr('src', e.target.result);
            }
            
            reader.readAsDataURL(input.files[0]);
        }
    }
    /***
    Scipt to display modal to add or edit recipe's ingredients
    ***/
    $(".add-ingredient").on('click', function (e) {
            e.preventDefault();
            const count = parseInt($(this).attr("id"));
            const url = $(this).attr("href");
            const addForm = $("#add-ingredient-form-" + count);
            addForm.attr("action", url);
            $("#add-ingredient-" + count).modal('show');
        })
    $(".edit-ingredient").on('click', function (e) {
            e.preventDefault();
            const count = parseInt($(this).attr("id"));
            const url = $(this).attr("href");
            const addForm = $("#edit-ingredient-form-" + count);
            addForm.attr("action", url);
            $("#edit-ingredient-" + count).modal('show');
        })
    /***
    Scipt to display ingredients in a datatable
    ***/
    $('#ingredients_table').DataTable(
        {
            'scrollX': true
        } 
    );

})
;
