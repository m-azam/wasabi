

function onLogin() {

    console.log("Incoming login req")
    var data = JSON.stringify({
        "uname": document.getElementById("login_uname").value,
        "password": document.getElementById("login_password").value
    });
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            var response = JSON.parse(this.responseText);
            if (response.login_status_flag == 1) {
                localStorage.setItem(username, document.getElementById("login_uname").value)
                window.location.href = "/qna_Section.html";
            } else {
                alert("Username or password is wrong!")
            }
        }
    });

    xhr.open("POST", "http://b649-149-164-110-192.ngrok.io/authentication/login");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.send(data);

}

function onSignUp() {
    var qr_code_base = ""
    console.log("Incoming sign up req")
    var data = JSON.stringify({
        "uname": document.getElementById("sign_uname").value,
        "password": document.getElementById("sign_password").value,
        "student_id": document.getElementById("student_id").value
    });
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            var response = JSON.parse(this.responseText);

            if (response.signup_status_flag == 1) {
                qr_code_base = response.qr_code
                document.getElementById('qr_issue_code')
                    .setAttribute(
                        'src', qr_code_base
                    );
            } else {
                alert("Username or password is wrong!")
            }
        }
    });

    xhr.open("POST", "http://b649-149-164-110-192.ngrok.io/authentication/register");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.send(data);

}

function verifyLogin() {
    console.log("Incoming verify req")
    var xhr = new XMLHttpRequest();
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            var response = JSON.parse(this.responseText);

            qr_code_base = response.qr_code
            document.getElementById('qr_issue_code')
                .setAttribute(
                    'src', qr_code_base
                );
        }
    });

    xhr.open("GET", "http://b649-149-164-110-192.ngrok.io/verify");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.send();

}


function getScore() {
    
    var xhr = new XMLHttpRequest();
    var score;
    xhr.withCredentials = true;

    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
            var response = JSON.parse(this.responseText);

            score = response.score
            document.getElementById('score').innerHTML='Your latest score is: 100';
        }
    });

    xhr.open("GET", "http://b649-149-164-110-192.ngrok.io/get_score");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.send();

}