const pwdInput = document.getElementById("password");
const toggle = document.getElementById("toggle");
const scoreText = document.getElementById("score");
const strengthText = document.getElementById("strength");
const crackTimeText = document.getElementById("crackTime");
const strengthFill = document.getElementById("strength-fill");
const suggestionsList = document.getElementById("suggestions");
const insightsList = document.getElementById("insights");
const breachWarning = document.getElementById("breachWarning");

const COMMON = ["password","123456","12345678","qwerty","admin","welcome","abc123"];

/* Toggle password visibility */
toggle.addEventListener("click", () => {
  pwdInput.type = pwdInput.type === "password" ? "text" : "password";
  toggle.textContent = pwdInput.type === "password" ? "Show" : "Hide";
});

/* Main logic */
pwdInput.addEventListener("input", () => {
  const pwd = pwdInput.value;
  let score = 0;
  let suggestions = [];

  /* Reset UI */
  breachWarning.style.display = "none";
  suggestionsList.innerHTML = "";
  insightsList.innerHTML = "";

  /* Scoring rules */
  if (pwd.length >= 8) score += 25;
  else suggestions.push("Increase length to at least 8 characters.");

  if (/[A-Z]/.test(pwd)) score += 15;
  else suggestions.push("Add at least one uppercase letter.");

  if (/[a-z]/.test(pwd)) score += 15;
  else suggestions.push("Add at least one lowercase letter.");

  if (/[0-9]/.test(pwd)) score += 20;
  else suggestions.push("Include at least one number.");

  if (/[^a-zA-Z0-9]/.test(pwd)) score += 25;
  else suggestions.push("Use at least one special character.");

  /* Pattern warnings */
  if (
    COMMON.includes(pwd.toLowerCase()) ||
    /(.)\1{2,}/.test(pwd)
  ) {
    breachWarning.style.display = "block";
  }

  /* Strength with icons (Option C) */
  let strength = "⚠️ Weak";
  let color = "#ef4444";

  if (score > 80) {
    strength = "🔒 Very Strong";
    color = "#22c55e";
  } else if (score > 60) {
    strength = "🟢 Strong";
    color = "#38bdf8";
  } else if (score > 30) {
    strength = "🟡 Medium";
    color = "#facc15";
  }

  /* Update UI */
  strengthFill.style.width = `${score}%`;
  strengthFill.style.background = color;
  scoreText.textContent = score;
  strengthText.textContent = strength;
  crackTimeText.textContent = estimateCrackTime(pwd);

  /* Suggestions */
  if (suggestions.length === 0 && pwd.length > 0) {
    suggestionsList.innerHTML = "<li>✔ Your password looks secure.</li>";
  } else {
    suggestions.forEach(text => {
      const li = document.createElement("li");
      li.textContent = text;
      suggestionsList.appendChild(li);
    });
  }

  /* Security Insights (Option A) */
  if (pwd.length > 0) {
    if (pwd.length < 8) {
      insightsList.innerHTML += "<li>Short passwords drastically reduce the number of possible combinations, making brute-force attacks faster.</li>";
    }

    if (/123|abc|qwerty/i.test(pwd)) {
      insightsList.innerHTML += "<li>Sequential or predictable patterns are commonly targeted in dictionary-based attacks.</li>";
    }

    if (COMMON.includes(pwd.toLowerCase())) {
      insightsList.innerHTML += "<li>Common passwords are often found in leaked databases and can be cracked instantly.</li>";
    }

    if (/(.)\1{2,}/.test(pwd)) {
      insightsList.innerHTML += "<li>Repeated characters lower entropy and weaken password strength.</li>";
    }

    if (insightsList.innerHTML === "") {
      insightsList.innerHTML = "<li>Your password shows no common structural weaknesses.</li>";
    }
  }
});

/* Crack time estimation */
function estimateCrackTime(pwd) {
  if (!pwd) return "–";

  let charset = 0;
  if (/[a-z]/.test(pwd)) charset += 26;
  if (/[A-Z]/.test(pwd)) charset += 26;
  if (/[0-9]/.test(pwd)) charset += 10;
  if (/[^a-zA-Z0-9]/.test(pwd)) charset += 32;

  const seconds = Math.pow(charset, pwd.length) / 1e10;

  if (seconds < 1) return "< 1 second";
  if (seconds < 60) return "Seconds";
  if (seconds < 3600) return "Minutes";
  if (seconds < 86400) return "Hours";
  if (seconds < 31536000) return "Days";
  return "Years+";
}
