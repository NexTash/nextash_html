window.onscroll = function () { navbar() };

function navbar() {
    let pos = 20
    if (document.body.scrollTop > pos || document.documentElement.scrollTop > pos) {
        document.getElementById("navbar").classList.add("bg-dark");
    } else {
        document.getElementById("navbar").classList.remove("bg-dark");
    }
}