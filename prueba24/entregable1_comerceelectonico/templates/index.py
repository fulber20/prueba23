<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recomendaciones de Productos</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Recomendaciones de Productos</h1>
    <form id="recommendation-form">
        <label for="user-id">ID del Usuario:</label>
        <input type="text" id="user-id" name="user-id">
        <button type="submit">Obtener Recomendaciones</button>
    </form>
    <div id="recommendations"></div>
    <script>
        document.getElementById('recommendation-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const userId = document.getElementById('user-id').value;

            fetch(`/recommendations?user-id=${userId}`)
                .then(response => response.json())
                .then(data => {
                    const recommendationsDiv = document.getElementById('recommendations');
                    recommendationsDiv.innerHTML = `<h2>Recomendaciones para el usuario ${data.user_id}</h2><ul>${data.recommended_products.map(product => `<li>${product}</li>`).join('')}</ul>`;
                });
        });
    </script>
</body>
</html>
