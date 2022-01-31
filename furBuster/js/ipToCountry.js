$.get("http://ipinfo.io", function (response) {
    // $("#ip").html("IP: " + response.ip);
    // $("#address").html("Location: " + response.city + ", " + response.region);
    // $("#details").html(JSON.stringify(response, null, 4));
    let btn = document.createElement("button");
    btn.innerHTML = "Klik hier";
    btn.type = "submit";
    btn.name = "formBtn";
    btn.onclick = function doggy() {
        alert("Button is clicked");
    };
    btn.addEventListener("click", function doggy() {
        alert("Button is clicked");
      });
    document.body.appendChild(btn);
    if (response.country == "NL"){
        if (response.vpn == false){
            $("#access").html("Klik op de knop om te starten.");
            $("#btnStart").html("Start");
        }
        else if (response.vpn == true){
            $("#access").html("VPN connections are not allowed for this service.");
        }
    else if (response.country != "NL"){
        $("#access").html("Only users from The Netherlands may access this service.");
    }
}
}, "jsonp");