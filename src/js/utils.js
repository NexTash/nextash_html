window.onscroll = function () { scroller() };

function scroller() {
    let pos = 20
    if (document.body.scrollTop > pos || document.documentElement.scrollTop > pos) {
        document.getElementById("navbar").classList.add("backdrop-8");
    } else {
        document.getElementById("navbar").classList.remove("backdrop-8");
    }
}