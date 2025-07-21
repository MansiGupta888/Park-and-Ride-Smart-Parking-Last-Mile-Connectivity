// frontend/js/booking.js
document.getElementById('bookingForm').addEventListener('submit', async (e) => {
  e.preventDefault();

  const booking = {
    user_email: document.getElementById('user_email').value,
    location: document.getElementById('location').value,
    duration: document.getElementById('duration').value
  };

  const res = await fetch('http://localhost:8000/booking/reserve', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(booking)
  });

  const data = await res.json();
  document.getElementById('msg').innerText = data.booking_id
    ? `Booked! ID: ${data.booking_id}` : 'Booking failed';
});
