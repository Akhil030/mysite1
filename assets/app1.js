function naveAnimation() {
    const nave = document.querySelector(".nav-header");
    const timeNav = gsap.timeline({
        defaults: { duration: '1.25', ease: "bounce.out" }
    });
    timeNav.fromTo(nave, { y: '-100%' }, { y: '0%' });
}
naveAnimation();

const curser = document.querySelector(".curser");
function mouse(e) {
    curser.style.top = e.pageY + 'px';
    curser.style.left = e.pageX + 'px';
}
window.addEventListener("mousemove", mouse);

const moreText = curser.querySelector("span");
function activeCurser(e) {
    const iteam = e.target;
    if (iteam.classList.contains("more") || iteam.classList.contains("view") || iteam.classList.contains("button-submit")) {
        curser.classList.add("curtser-naver");
        curser.classList.add("curtser-logo");
        moreText.innerText = "Tap";
    }
    else {
        curser.classList.remove("curtser-naver");
        curser.classList.remove("curtser-logo");
        moreText.innerText = "";
    }
}
window.addEventListener("mouseover", activeCurser);




