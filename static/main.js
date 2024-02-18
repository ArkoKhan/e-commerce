const password01 = document.querySelector("#password001");
const password02 = document.querySelector("#password002");
const msgPass = document.querySelector(".msg_pass");

password02.addEventListener("input", function () {
  if (password01.value != password02.value) {
    msgPass.innerHTML = `<span class="msg_warning">Your Password did not match.</span>`;
  } else {
    msgPass.innerHTML = `<span class="msg_success">Your Password matched.</span>`;
  }
});
