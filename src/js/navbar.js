let psp = window.pageYOffset;
window.onscroll = function () {
    let csp = window.pageYOffset;
    if (psp > csp) {
        document.getElementById("navbar").style.top = "0";
    } else {
        document.getElementById("navbar").style.top = "-50px";
    }
    psp = csp;
}