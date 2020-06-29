// Changing the sign up button color when hovering over it
var newbutton = {
    "background":"rgb(144, 12, 63, 0.8)",
    "color":"white"       
}
var oldbutton = {
    "background":"transparent",
    "color":"black"      
}
var button = $("#sign")


function buttonanimation() {
    button.mouseover(function () {
        button.css(newbutton);
        button.text("Join the Cookbook now!");
    })
    button.mouseout(function () {
        button.css(oldbutton);
        button.text("Sign up to join the Cookbook");
    })
}


buttonanimation()



// Changing the check my recipes button color when hovering over it (welcome @user page)
var newbut = {
    "background":"rgb(144, 12, 63, 0.76)", 
    "color":"white"      
}
var oldbut = {
    "background":"transparent",
    "color":"black"       
}
var btn = $("#userrecipes")


function butnanimation() {
    btn.mouseover(function () {
        btn.css(newbut);
    })
    btn.mouseout(function () {
        btn.css(oldbut);
    })
}

butnanimation()


// landing page signed in -> changing final buttons at bottom from transparent background to red
all = [$("#all"),$("#cat"),$("#new"),$("#user")]

function ColHelp(fields) {
    var newbut = {
        "background":"rgb(144, 12, 63, 0.8)"   ,
    }
    var oldbut = {
        "background":"transparent"
    } 
    fields.mouseover(function() {
        fields.css(newbut);
    })
    fields.mouseout(function(){
        fields.css(oldbut)
    })
}

function colorFields(id) {   
    for (i in id) {
            ColHelp(id[i]);
    }
}

colorFields(all)


// navbar items -> red color when hovering above them:
navbar = [$("#brand"),$("#greeting"),$("#recipes"),$("#create"),$("#bye"),$("#signup"),$("#login"),$("#about")]

function ColSup(fields) {
    var newbut = {
        "color":"rgb(144, 12, 63)"       
    }
    var oldbut = {
        "color":"white"
    } 
    fields.mouseover(function() {
        fields.css(newbut);
    })
    fields.mouseout(function(){
        fields.css(oldbut);
    })
}

function colorNavbar(id) {   
    for (i in id) {
            ColSup(id[i]);
    }
}

colorNavbar(navbar)


// Alertify library to send push up notifications: https://alertifyjs.com/

function notification(text) {
    alertify.set("notifier","position","top-right");
    alertify.success(text);
}



