// FAQ accordion
document.querySelectorAll('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.faq-item');
    const isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
    if (!isOpen) item.classList.add('open');
  });
});

// Mobile nav
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
if (hamburger) {
  hamburger.addEventListener('click', () => {
    navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
    navLinks.style.flexDirection = 'column';
    navLinks.style.position = 'absolute';
    navLinks.style.top = '64px';
    navLinks.style.left = '0';
    navLinks.style.right = '0';
    navLinks.style.background = 'white';
    navLinks.style.padding = '16px 2rem';
    navLinks.style.borderBottom = '1px solid #e5e9f0';
    navLinks.style.zIndex = '99';
  });
}

// Active nav link
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-links a').forEach(a => {
  if (a.getAttribute('href') === currentPage) a.classList.add('active');
});

// Prediction form with loading animation
// Prediction form with loading animation
const predictForm = document.getElementById('predictForm');

if (predictForm) {

    predictForm.addEventListener('submit', function(e) {

        e.preventDefault();

        const overlay = document.getElementById('loadingOverlay');
        const bar = document.getElementById('progressBar');

        overlay.classList.add('active');

        setTimeout(() => {
            bar.style.width = '100%';
        }, 50);

        setTimeout(() => {
            this.submit();
        }, 1800);

    });

}
// Dashboard — load results
if (document.getElementById('dashboardResult')) {
  const raw = sessionStorage.getItem('patientData');
  if (raw) {
    const d = JSON.parse(raw);
    const isHigh = d.prediction === 'high';
    const conf = d.confidence;

    // patient summary
    const genderMap = { '0': 'Female', '1': 'Male' };
    const cpMap = { '0': 'Typical Angina', '1': 'Atypical Angina', '2': 'Non-Anginal', '3': 'Asymptomatic' };
    document.getElementById('pAge').textContent = d.age || '—';
    document.getElementById('pGender').textContent = genderMap[d.gender] || '—';
    document.getElementById('pBP').textContent = d.trestbps ? d.trestbps + ' mmHg' : '—';
    document.getElementById('pChol').textContent = d.chol ? d.chol + ' mg/dl' : '—';
    document.getElementById('pCP').textContent = cpMap[d.cp] || '—';
    document.getElementById('pHR').textContent = d.thalach ? d.thalach + ' bpm' : '—';

    // prediction
    const badge = document.getElementById('riskBadge');
    badge.className = 'risk-badge ' + (isHigh ? 'risk-high' : 'risk-low');
    badge.innerHTML = `<span class="risk-dot"></span>${isHigh ? '🔴 High Risk' : '🟢 Low Risk'}`;
    document.getElementById('riskExplain').textContent = isHigh
      ? 'Your health indicators suggest an increased likelihood of heart disease. This is not a diagnosis — please consult a qualified healthcare professional.'
      : 'Your health indicators suggest a lower likelihood of heart disease. Keep maintaining your current healthy lifestyle.';

    // confidence
    document.getElementById('confNum').textContent = conf + '%';

    // risk meter
    const lowBar = document.getElementById('meterLow');
    const modBar = document.getElementById('meterMod');
    const highBar = document.getElementById('meterHigh');
    if (isHigh) {
      highBar.style.width = conf + '%'; highBar.style.background = '#dc2626';
      modBar.style.width = '40%'; modBar.style.background = '#d97706';
      lowBar.style.width = '20%'; lowBar.style.background = '#16a34a';
      document.getElementById('meterHighRow').style.fontWeight = '700';
    } else {
      lowBar.style.width = conf + '%'; lowBar.style.background = '#16a34a';
      modBar.style.width = '30%'; modBar.style.background = '#d97706';
      highBar.style.width = '15%'; highBar.style.background = '#dc2626';
      document.getElementById('meterLowRow').style.fontWeight = '700';
    }

    // recommendations
    const recsContainer = document.getElementById('recommendations');
    const lowRecs = [
      { icon: '🥗', text: 'Maintain a balanced diet rich in fruits and vegetables' },
      { icon: '🏃', text: 'Continue regular physical activity (30 min/day)' },
      { icon: '🩺', text: 'Schedule annual health checkups' },
      { icon: '😴', text: 'Ensure 7–8 hours of quality sleep each night' },
    ];
    const highRecs = [
      { icon: '👨‍⚕️', text: 'Consult a cardiologist as soon as possible' },
      { icon: '💊', text: 'Follow prescribed medications strictly' },
      { icon: '📊', text: 'Monitor blood pressure and cholesterol regularly' },
      { icon: '🚭', text: 'Avoid smoking, alcohol, and high-sodium foods' },
    ];
    const recs = isHigh ? highRecs : lowRecs;
    recsContainer.innerHTML = recs.map(r => `
      <div class="rec-item">
        <span class="rec-icon">${r.icon}</span>
        <span class="rec-text">${r.text}</span>
      </div>`).join('');
  } else {
    document.getElementById('dashboardResult').innerHTML = '<p style="color:var(--text-muted);padding:32px;">No prediction data found. <a href="predict.html">Run a prediction first.</a></p>';
  }
}

// BMI Calculator
const bmiForm = document.getElementById('bmiForm');
if (bmiForm) {
  bmiForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const h = parseFloat(document.getElementById('height').value) / 100;
    const w = parseFloat(document.getElementById('weight').value);
    const bmi = (w / (h * h)).toFixed(1);
    let cat, color, tips;
    if (bmi < 18.5) {
      cat = 'Underweight'; color = '#d97706';
      tips = ['Increase calorie intake with nutrient-rich foods', 'Add strength training to build muscle mass', 'Consult a nutritionist for a personalised plan'];
    } else if (bmi < 25) {
      cat = 'Normal weight ✓'; color = '#16a34a';
      tips = ['Maintain your current diet and exercise routine', 'Stay hydrated and prioritise sleep', 'Keep up with regular health screenings'];
    } else if (bmi < 30) {
      cat = 'Overweight'; color = '#d97706';
      tips = ['Reduce intake of processed and high-fat foods', 'Aim for 150 min of moderate exercise per week', 'Consider speaking to a dietitian'];
    } else {
      cat = 'Obese'; color = '#dc2626';
      tips = ['Seek medical guidance for a weight management plan', 'Focus on sustainable lifestyle changes', 'Monitor heart health indicators regularly'];
    }
    document.getElementById('bmiNum').textContent = bmi;
    document.getElementById('bmiCat').textContent = cat;
    document.getElementById('bmiCat').style.color = color;
    document.getElementById('bmiTips').innerHTML = tips.map(t => `<div class="bmi-tip"><span>→</span><span>${t}</span></div>`).join('');
    document.getElementById('bmiResult').style.display = 'block';
  });
}

// Contact form
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault();
    document.getElementById('successMsg').style.display = 'block';
    contactForm.reset();
    setTimeout(() => { document.getElementById('successMsg').style.display = 'none'; }, 4000);
  });
}
