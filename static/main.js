const password = document.querySelectorAll(".pass_class");
const msgPass = document.querySelector(".msg_pass");

for (let i = 0; i < password.length; i++) {
  password[i].addEventListener("input", function () {
    if (password[0].value != password[1].value) {
      msgPass.innerHTML = `<span class="msg_warning">Your Password did not match.</span>`;
    } else if (password[0].value == "" && password[1].value == "") {
      msgPass.innerHTML = "";
    } else {
      msgPass.innerHTML = `<span class="msg_success">Your Password matched.</span>`;
    }
  });
}
