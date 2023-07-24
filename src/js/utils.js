window.onscroll = function () { scroller() };

function scroller() {
    let pos = 20
    if (document.body.scrollTop > pos || document.documentElement.scrollTop > pos) {
<<<<<<< HEAD
        document.getElementById("navbar").classList.add("bg-dark");
=======
        document.getElementById("navbar").classList.add("backdrop-8");
>>>>>>> d8a3eef3ae8178c21dd7c93bd8651368bf93045f
    } else {
        document.getElementById("navbar").classList.remove("backdrop-8");
    }
}