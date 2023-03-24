function showPopup() {
    $("#popup-form").show();
}

function showPopupAddChild() {
    $("#popup-form-add-child").show();
}

function submitForm() {
    let text = $("#textfield").val();

    $.post("/submit_text", { textfield: text }, function (data) {
        alert(data);
        $("#popup-form").hide();
    });

    return false;
}

function submitFormChild() {
    let nameChild = $("#nameChild").val();
    let indexParent = $("#indexParent").val();
    $.post("/submit_child", { nameChild: nameChild, indexParent: indexParent }, function (data) {
        alert(data);
        $("#popup-form-add-child").hide();
    });

    return false;
}
