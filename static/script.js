document.getElementById('personaForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const productInfo = document.getElementById('product_info').value;
    const audienceInfo = document.getElementById('audience_info').value;
  
    const requestData = {
      product_info: productInfo,
      audience_info: audienceInfo
    };
  
    fetch('http://127.0.0.1:3000/generate_persona', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(requestData),
    })
    .then(response => response.json())
    .then(data => {
      document.getElementById('personaResult').innerText = data.persona;
    })
    .catch(error => {
      console.error('Error:', error);
      document.getElementById('personaResult').innerText = 'There was an error generating the persona.';
    });
  });
  