const encryptedUsername = btoa("tartarus2024");
const encryptedPassword = btoa("vacas123");

function login() {
  const userInput = document.getElementById("username").value;
  const passInput = document.getElementById("password").value;
  const errorMsg = document.getElementById("errorMsg");

  if (btoa(userInput) === encryptedUsername && btoa(passInput) === encryptedPassword) {
    document.getElementById("loginContainer").style.display = "none";
    document.getElementById("mainContent").classList.remove("hidden");
    // Guardar estado de login
    localStorage.setItem('isLoggedIn', 'true');
  } else {
    errorMsg.textContent = "Usuario o contraseña incorrectos";
    errorMsg.style.color = "red";
  }
}

// For smoother UX if user presses Enter
window.addEventListener("keydown", function (e) {
  if (e.key === "Enter") login();
});

// Verificar si el usuario ya está logueado
document.addEventListener('DOMContentLoaded', function() {
  if (localStorage.getItem('isLoggedIn') === 'true') {
    document.getElementById("loginContainer").style.display = "none";
    document.getElementById("mainContent").classList.remove("hidden");
  }
});

// Función para copiar el enlace de Discord
function copyDiscordLink() {
  const discordInput = document.querySelector('.discord-link input');
  discordInput.select();
  document.execCommand('copy');
  
  const button = document.querySelector('.discord-link .action-button');
  const originalText = button.textContent;
  button.textContent = '¡Copiado!';
  setTimeout(() => {
    button.textContent = originalText;
  }, 2000);
}

// Mejorar la experiencia táctil en la tabla
document.addEventListener('DOMContentLoaded', function() {
  const table = document.querySelector('.timeline-table');
  if (table) {
    let touchStartX;
    let touchEndX;

    table.addEventListener('touchstart', function(e) {
      touchStartX = e.touches[0].clientX;
    });

    table.addEventListener('touchmove', function(e) {
      touchEndX = e.touches[0].clientX;
    });

    table.addEventListener('touchend', function() {
      if (touchStartX - touchEndX > 50) {
        table.scrollLeft += 100;
      } else if (touchEndX - touchStartX > 50) {
        table.scrollLeft -= 100;
      }
    });
  }
});

// Función para verificar y manejar el estado del botón de documentos legales
document.addEventListener('DOMContentLoaded', function() {
  const legalDocsLink = document.querySelector('.legal-docs-link');
  const legalDocsButton = document.querySelector('.legal-docs-link .cta-button');
  
  if (legalDocsLink && legalDocsButton) {
    // Verificar si el enlace está vacío o no es válido
    if (!legalDocsLink.getAttribute('href') || legalDocsLink.getAttribute('href') === '') {
      legalDocsLink.removeAttribute('href');
      legalDocsButton.classList.remove('active-button');
      legalDocsButton.classList.add('disabled-button');
    } else {
      legalDocsButton.classList.add('active-button');
      legalDocsButton.classList.remove('disabled-button');
    }
  }
  
  // Identificar y marcar botones sin enlaces
  const allButtons = document.querySelectorAll('.cta-button');
  allButtons.forEach(button => {
    // Verificar si el botón está dentro de un enlace
    const parentLink = button.closest('a');
    if (!parentLink || !parentLink.getAttribute('href') || parentLink.getAttribute('href') === '') {
      button.classList.add('no-link');
    }
  });
});
