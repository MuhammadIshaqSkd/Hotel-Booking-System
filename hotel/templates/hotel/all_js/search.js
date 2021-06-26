    <script>

        {% if msg|length != 0 %}
        alert('{{msg}}');
        window.location.href = "/hotel"
        {% endif %}

    </script>