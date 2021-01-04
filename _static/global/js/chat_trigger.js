console.log("engines running: alert chats");

function triggerMessage(chatID){
	var element = chatID;
	document.getElementById(element).className += " show";
}

document.getElementById("buttonA1").addEventListener("click", function() {
    triggerMessage("Q2");
    // triggerMessage("Q2.1");
    // triggerMessage("Q2.2");
    // triggerMessage("A2");
}, false);

document.getElementById("buttonA2").addEventListener("click", function() {
    triggerMessage("Q3");
    // triggerMessage("Q3.1");
    // triggerMessage("Q3.2");
    // triggerMessage("A3");
}, false);

document.getElementById("buttonA3").addEventListener("click", function() {
    // triggerMessage("Q4");
    triggerMessage("submit_button")
}, false);