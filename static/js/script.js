let currentValue = 0;

function animateValue(obj, start, end, duration) {
  if (start == end) return;
  let startTimestamp = null;
  const step = (timestamp) => {
    document.getElementById('lastUpdate').innerText = Date()
    if (!startTimestamp) startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    currentValue = progress * (end - start) + start;
    obj.innerText = `${currentValue.toLocaleString('en-US', {style: 'currency', currency: 'USD'})}`
    if (progress < 1) {
      window.requestAnimationFrame(step);
    }
  };
  window.requestAnimationFrame(step);
}

function updateDonatedValue(isFirst) {
  fetch('/api/v1/donated')
  .then((resp) => resp.json())
  .then((data) => {
    const newValue = data.donated_usd;
    animateValue(document.getElementById('donated'), currentValue, newValue, isFirst ? 1500 : 60000);
  });
};

updateDonatedValue(true);
setInterval(updateDonatedValue, 60000);
