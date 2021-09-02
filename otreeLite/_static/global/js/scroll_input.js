console.log("scroll prevention ready!")

// disable scrolling on number-input
document.addEventListener("wheel", function(event){
    if(document.activeElement.type === "number"){
        document.activeElement.blur();
    }
});