// add_parent popup
function hideAllPopups() {
    $('.popup').hide();
  }
  
  
  function showPopup() {
    hideAllPopups();
    $("#popup-form").show();
    $("#textfield").focus();
  }

function closeForm(){
    $('#popup-form').hide();
}

function submitForm() {
    let text = $("#textfield").val();

    $.post("/submit_text", { textfield: text }, function (data) {
        alert(data);
        $("#popup-form").hide();
        location.reload();
    });

    $("#textfield").val('');

    return false;
}

// add_child popup
function showPopupAddChild() {
    hideAllPopups();
    $("#popup-form-add-child").show();
    $("#nameChild").focus();
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

    $("#nameChild").val('');
    $('#indexParent').val('');

    return false;
}

// delete_parent popup

function showPopupDeleteParent() {
    hideAllPopups();
    $("#popup-form-delete-parent").show();
    $("#nameParent").focus();
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
    
    $("#nameParent").val('');

    return false;
}

// delete_child popup

function showPopupDeleteChild() {
    hideAllPopups();
    $("#popup-form-delete-child").show();
    $("#indexParent_DeleteChild").focus();
  }

function closeFormDeleteChild() {
    $('#popup-form-delete-child').hide();
}

function submitFormDeleteChild() {

    let indexParent = $("#indexParent_DeleteChild").val();
    let indexChild = $("#indexChild_DeleteChild").val();
    $.post("/delete_child", { indexParent: indexParent, indexChild: indexChild }, function (data) {
        alert(data);
        $("#popup-form-delete-child").hide();
        location.reload();
    });

    $("#indexParent_DeleteChild").val('');
    $("#indexChild_DeleteChild").val('');

    return false;
}


// key commands

document.addEventListener('keydown', function(event) {

    if(
        event.key==='a' &&

        $("#popup-form-add-child").is(":hidden") && $("#popup-form-delete-child").is(":hidden") && $("#popup-form-delete-parent").is(":hidden")

        ) {
        showPopup();
    }
    else if(
        event.key==='c' && 
        $("#popup-form").is(":hidden") && $("#popup-form-delete-child").is(":hidden") && $("#popup-form-delete-parent").is(":hidden")
        ) {
        showPopupAddChild();
    }
    else if (
        event.key === 'A' && 
        event.shiftKey && 
        $("#popup-form").is(":hidden") && $("#popup-form-add-child").is(":hidden") && $("#popup-form-delete-child").is(":hidden")
        ) {
        showPopupDeleteParent();
    }
    else if(
        event.key === 'C' && 
        event.shiftKey && 
        $("#popup-form").is(":hidden") && $("#popup-form-add-child").is(":hidden") && $("#popup-form-delete-parent").is(":hidden")
        ) {
        showPopupDeleteChild();
    }
});

// dark light mode switch

var themeChange = document.getElementById('theme-switch');

function themeSwap() {
    document.body.classList.toggle('light-theme');
}


