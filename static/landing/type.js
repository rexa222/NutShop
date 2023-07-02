const descriptionElement = document.getElementById("typing-effect");
const textArray = [
    "کیفیت، اصالت، حس خوب",
    "ناب ترین مغزها از بهترین مزارع ایران",
    "تا درب منازل شما..."
];
const typingDelay = 100; // Delay between each character being typed
const erasingDelay = 50; // Delay between each character being erased
const newTextDelay = 2000; // Delay between typing and erasing the word
let textArrayIndex = 0;
let charIndex = 0;
let typing = true;

function type() {
    if (typing) {
        if (charIndex < textArray[textArrayIndex].length) {
            descriptionElement.innerHTML += textArray[textArrayIndex].charAt(charIndex);
            charIndex++;
            setTimeout(type, typingDelay);
        } else {
            setTimeout(erase, newTextDelay);
        }
    }
}

function erase() {
    if (typing) {
        if (charIndex > 0) {
            descriptionElement.innerHTML = textArray[textArrayIndex].substring(0, charIndex - 1);
            charIndex--;
            setTimeout(erase, erasingDelay);
        } else {
            textArrayIndex++;
            if (textArrayIndex >= textArray.length) {
                textArrayIndex = 0;
            }
            setTimeout(type, typingDelay);
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    if (textArray.length) {
        setTimeout(type, newTextDelay);
    }
});
