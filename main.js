const encryptedUsername = btoa("tartarus2024");
const encryptedPassword = btoa("vacas123");

function login() {
  const userInput = document.getElementById("username").value;
  const passInput = document.getElementById("password").value;
  const errorMsg = document.getElementById("errorMsg");

  if (btoa(userInput) === encryptedUsername && btoa(passInput) === encryptedPassword) {
    document.getElementById("loginContainer").style.display = "none";
    document.getElementById("mainContent").classList.remove("hidden");
  } else {
    errorMsg.textContent = "Usuario o contraseña incorrectos";
    errorMsg.style.color = "red";
  }
}

// For smoother UX if user presses Enter
window.addEventListener("keydown", function (e) {
  if (e.key === "Enter") login();
});
