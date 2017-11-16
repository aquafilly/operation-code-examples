var coders = [];

function getCoderForEdit(ctl) {
    var id = $(ctl).data("id");
    $("#coderId").val(id);
    $.ajax({
        url: "/coders/" + id,
        type: 'GET',
        dataType: 'json',
        success: function (coder) {
            coderToEditFields(coder);
        },
        error: function (request, message, error) {
            handleException(request, message, error);
        }
    });
}

function getCoderForDelete(ctl) {
    var id = $(ctl).data("id");
    $("#coderId").val(id);
    $.ajax({
        url: "/coders/" + id,
        type: 'GET',
        dataType: 'json',
        success: function (coder) {
            coderToDeleteFields(coder);
        },
        error: function (request, message, error) {
            handleException(request, message, error);
        }
    });
}

function getCoders() {
    let query = '/coders';
    console.log('Making GET request: ' + query);
    window.fetch(query)
        .then(function (res) {
            console.log(res);
            return res.json();
        })
        .then(function (data) {
            updateCodersView(data);
        })
}

function updateCoder() {
    var body = {
        id: $("#coderId").val(),
        firstname: $("#firstNameEdit").val(),
        lastname: $("#lastNameEdit").val(),
        meetups: $("#meetupsEdit").val()
    };
    $.ajax({
        type: "PUT",
        url: "/coders/",
        contentType: 'application/json',
        data: JSON.stringify(body),
        success: function (coder) {
            $("#coderEditForm").css("display","none");
            getCoders();            
        },
        error: function (request, message, error) {
            handleException(request, message, error);
        }
    });
}

function deleteCoder() {
    var body = {
        id: $("#coderId").val()
    };
    $.ajax({
        type: "DELETE",
        url: "/coders/",
        contentType: 'application/json',
        data: JSON.stringify(body),
        success: function (coder) {
            $("#coderDeleteForm").css("display","none");
            getCoders();            
        },
        error: function (request, message, error) {
            handleException(request, message, error);
        }
    });
}

function cancelDeleteCoder() {
    $("#coderDeleteForm").css("display","none");
}

function coderToEditFields(coder) {
    $("#firstNameEdit").val(coder.firstname);
    $("#lastNameEdit").val(coder.lastname);
    $("#meetupsEdit").val(coder.meetups);
    $("#coderEditForm").removeAttr("style");
}

function coderToDeleteFields(coder) {
    $("#firstNameDelete").val(coder.firstname);
    $("#lastNameDelete").val(coder.lastname);
    $("#meetupsDelete").val(coder.meetups);
    $("#coderDeleteForm").removeAttr("style");
}

function updateCodersView(coders) {
    let codersElement = document.getElementById('codersTableBody');
    removeAllChildren(codersElement);

    coders.forEach(function (coder) {
        codersElement.appendChild(getCoderRow(coder));
    });
}

function getCoderRow(coder) {
    let coderRow = document.createElement('tr');
    coderRow.appendChild(getCell(coder.firstname));
    coderRow.appendChild(getCell(coder.lastname));
    coderRow.appendChild(getCell(coder.meetups));
    coderRow.appendChild(getEditCell(coder._id));
    coderRow.appendChild(getDeleteCell(coder._id));
    return coderRow;
}

function getCell(innerText) {
    let cell = document.createElement('td');
    cell.innerText = innerText;
    return cell;
}

function getEditCell(coderId) {
    let cell = document.createElement('td');
    cell.innerHTML = "<button type='button' " +
                        "onclick='getCoderForEdit(this);' " +
                         "data-id='" + coderId + "'>Edit" +
                    "</button>";
    return cell;
}

function getDeleteCell(coderId) {
    let cell = document.createElement('td');
    cell.innerHTML = "<button type='button' " +
                        "onclick='getCoderForDelete(this);' " +
                         "data-id='" + coderId + "'>Delete" +
                    "</button>";
    return cell;
}

function handleException(request, message, error) {
    var msg = "";
    msg += "Code: " + request.status + "\n";
    msg += "Text: " + request.statusText + "\n";
    if (request.responseJSON != null) {
        msg += "Message" +
            request.responseJSON.Message + "\n";
    }
    alert(msg);
}

function removeAllChildren(myNode) {
    if (!myNode.firstChild)
        return;
    while (myNode.firstChild) {
        myNode.removeChild(myNode.firstChild);
    }
}

getCoders();