// add_parent popup

function showPopup() {
    $("#popup-form").show();
}

function closeForm(){
    $('#popup-form').hide();
}

function submitForm() {
    let text = $("#textfield").val();

    $.post("/submit_text", { textfield: text }, function (data) {
        alert(data);
        $("#popup-form").hide();
    });

    return false;
}

// add_child popup
function showPopupAddChild() {
    $("#popup-form-add-child").show();
}

function closeFormAddChild() {
    $('#popup-form-add-child').hide();
}

function submitFormChild() {
    let nameChild = $("#nameChild").val();
    let indexParent = $("#indexParent").val();
    $.post("/submit_child", { nameChild: nameChild, indexParent: indexParent }, function (data) {
        alert(data);
        $("#popup-form-add-child").hide();
        location.reload();
    });

    return false;
}

// delete_parent popup

function showPopupDeleteParent() {
    $("#popup-form-delete-parent").show();  
}

function closeFormDeleteParent() {
    $('#popup-form-delete-parent').hide();  
}

function submitFormDeleteParent() {
    let indexParent = $("#nameParent").val();
    $.post("/delete_parent", { nameParent: indexParent }, function (data) {
        alert(data);
        $("#popup-form-delete-parent").hide();  
        location.reload();
    });

    return false;
}