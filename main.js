const encryptedUsername = btoa("tartarus2024");
const encryptedPassword = btoa("vacas123");

function login() {
  const userInput = document.getElementById("username").value;
  const passInput = document.getElementById("password").value;
  const errorMsg = document.getElementById("errorMsg");

  if (btoa(userInput) === encryptedUsername && btoa(passInput) === encryptedPassword) {
    document.getElementById("loginContainer").style.display = "none";
    document.getElementById("mainContent").classList.remove("hidden");
    
    // Initialize button functionality after login
    initializeButtons();
  } else {
    errorMsg.textContent = "Usuario o contraseña incorrectos";
    errorMsg.style.color = "red";
  }
}

// For smoother UX if user presses Enter
window.addEventListener("keydown", function (e) {
  if (e.key === "Enter") login();
});

// Initialize button functionality
function initializeButtons() {
  // Set up the "Sube tus datos legales aquí" button
  const legalDataButton = document.querySelector('.content-section:nth-child(4) .cta-button');
  if (legalDataButton) {
    legalDataButton.addEventListener('click', function() {
      window.open('https://drive.google.com/drive/folders/1Mdb3_kXdkEpPANT3jgvqGwlU3NvvfTkk?usp=sharing', '_blank');
    });
  }
  
  // Set up all other CTA buttons
  const allCtaButtons = document.querySelectorAll('.cta-button');
  allCtaButtons.forEach(button => {
    // Skip the legal data button as it's already handled
    if (button !== legalDataButton) {
      // Add inactive class to buttons without links
      button.classList.add('inactive');
      button.disabled = true;
    }
  });
  
  // Set up all action buttons
  const allActionButtons = document.querySelectorAll('.action-button');
  allActionButtons.forEach(button => {
    // Add inactive class to buttons without links
    button.classList.add('inactive');
    button.disabled = true;
  });
  
  // Set up the "Copiar enlace" button for Discord
  const copyDiscordButton = document.querySelector('.discord-link .action-button');
  if (copyDiscordButton) {
    copyDiscordButton.classList.remove('inactive');
    copyDiscordButton.disabled = false;
    copyDiscordButton.addEventListener('click', function() {
      const discordInput = document.querySelector('.discord-link input');
      if (discordInput) {
        discordInput.select();
        document.execCommand('copy');
        alert('Enlace copiado al portapapeles');
      }
    });
  }
}
