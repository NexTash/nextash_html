window.onscroll = function () { scroller() };

function scroller() {
    let pos = 20
    if (document.body.scrollTop > pos || document.documentElement.scrollTop > pos) {
        document.getElementById("navbar").classList.add("bg-dark");
    } else {
        document.getElementById("navbar").classList.remove("bg-dark");
    }
}