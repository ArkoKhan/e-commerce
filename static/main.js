const password01 = document.querySelector("#password001");
const password02 = document.querySelector("#password002");
const msg = document.querySelector(".msg");

password02.addEventListener("change", function () {
  if (password01.value != password02.value) {
    msg.innerHTML = `<span class="msg_warning">Your Password did not match.</span>`;
  } else {
    msg.innerHTML = `<span class="msg_success">Your Password matched.</span>`;
  }
});
