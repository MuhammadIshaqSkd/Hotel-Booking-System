

<script>
{% if thank %}
alert('Thanks for Booking with us. Your booking  id is {{id}}. Use it to check your booking status using our Booking Status');
document.location = "/hotel";
{% endif %}
</script>