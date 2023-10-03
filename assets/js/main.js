AOS.init();
VanillaTilt.init();

window.onscroll = function () {
  navbar();
};
function navbar() {
  let position = 20;
  if (
    document.body.scrollTop > position ||
    document.documentElement.scrollTop > position
  ) {
    document.getElementById("navbar").classList.add("navbar-dark");
  } else {
    document.getElementById("navbar").classList.remove("navbar-dark");
  }
}

document.querySelectorAll(".sidebarBtn").forEach(function (item) {
  item.addEventListener("click", function () {
    document.getElementById("sidebar").classList.toggle("hide");
  });
});
