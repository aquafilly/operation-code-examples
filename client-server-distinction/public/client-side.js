var buttonClicks = 0;

function onButtonClicked(event) {
    buttonClicks += 1;
    console.log("client: button clicked");
    console.log("client: local button click count is " + buttonClicks);    
    tellServerButtonWasClicked();
}

function tellServerButtonWasClicked() {
    window.fetch('/button')
    .then( (resp) => resp.json() )
    .then( function (data) {
        if(data.error) {
            window.alert(data.error);
        } else {
            console.log("client: server knows button was clicked");
            console.log("client: server button click count is " + data.clicks)
        }
    });
}