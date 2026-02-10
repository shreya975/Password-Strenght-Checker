# 🔐 Password Security Analyzer

A modern, security-focused password strength analyzer that evaluates passwords in real time using rule-based validation, pattern detection, entropy-based crack-time estimation, and actionable security insights — presented with a professional, product-grade web UI.

---

## 🚀 Features

### ✅ Core Security Analysis
- Password length validation
- Uppercase, lowercase, digit, and special character checks
- Real-time strength scoring (0–100)
- Strength classification: ⚠️ Weak, 🟡 Medium, 🟢 Strong, 🔒 Very Strong

### 🧠 Advanced Security Intelligence
- Detection of weak patterns (sequences, repeated characters)
- Common password detection using an external dataset
- Entropy-based crack-time estimation (GPU brute-force model)

### 💡 User Guidance
- Clear improvement suggestions
- Security insights explaining *why* a password is weak
- Breach-style warning for predictable or common passwords

### 🎨 Professional Web Interface
- Dark-mode, glassmorphism UI
- Animated strength meter
- Live feedback while typing
- Password visibility toggle
- Clean, SaaS-style design

---

## 🖥️ Tech Stack

**Backend / Logic**
- Python
- Regex-based validation
- Modular architecture (validator, scorer, patterns, suggestions)

**Frontend**
- HTML5
- CSS3 (Glassmorphism, animations)
- Vanilla JavaScript (real-time analysis)

---

## 📸 Preview

> Screenshots show:
> - Empty state
> - Weak password analysis
> - Strong password analysis with crack-time estimation

*(Screenshots included in repository)*

---

## 📂 Project Structure

password-strength-analyzer/
│
├── src/
│ ├── validator.py
│ ├── scorer.py
│ ├── patterns.py
│ └── suggestions.py
│
├── data/
│ └── common_passwords.txt
│
├── web/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── main.py
└── README.md


---

## ▶️ How to Run

### Web Version
1. Open `web/index.html` in your browser
2. Start typing a password to see real-time analysis

### Python (CLI Version)
```bash
python main.py
