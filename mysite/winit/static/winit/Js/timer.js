function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    var counter = setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            clearInterval(counter);
            alert("Time Up!!");
            document.getElementById('submit').click()
            
        }
    }, 1000);
}

window.onload = function () {
    var fiveMinutes = 5,
        display = document.getElementById("time");
    startTimer(fiveMinutes, display);
};