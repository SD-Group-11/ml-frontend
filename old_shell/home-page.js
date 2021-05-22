const canvas = document.getElementById("thecanvas");

const graphics = canvas.getContext("2d");
const model_selector = document.getElementById("models");
const model_selector_div = document.getElementById("modelsDiv");
const help_button = document.getElementById("helpBtn")

graphics.strokeStyle ="White";
graphics.translate(190,230);
graphics.scale(2,2);
graphics.strokeText("Visualisation of Models will occur here.",0,0);


model_selector.addEventListener("change",() =>{
    var selected_model = model_selector.options[model_selector.selectedIndex].text;
    if (selected_model != 'None'){
    var tutorial_button = document.createElement("input");
    tutorial_button.id = "tutorial_button";
    tutorial_button.type = "button";
    tutorial_button.value = "How to use The " +selected_model + " Model?";
    tutorial_button.className= "button";
    model_selector_div.append(tutorial_button);}
})
document.addEventListener('click',function(e){
    if(e.target && e.target.id== 'tutorial_button'){
        window.location.href ="documentation.html";        
     }
 });

help_button.addEventListener('click',()=>{
    window.location.href ="documentation.html";        
})