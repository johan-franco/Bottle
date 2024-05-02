<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{{name}} in {{place}}</title>
<style type="text/css">
body {
    margin: 25px;
    padding: 25px;
}
h1 {
    text-align: center;
}
main {
    border: 1px dotted #555;
}
main p {
    padding: 10px;
}
a, a:visited {
    color: #663;
    text-decoration: none;
}
footer {
    text-align: center;
    margin-top: 20px;
}
</style>
<script>
function add_validation_links() {
  var loc = window.location.href;
  var HTMLvalidLinkStr = 'http://validator.w3.org/check?uri=' + loc;
  var CSSvalidLinkStr = 'http://jigsaw.w3.org/css-validator/validator?uri=' +
                        loc + '?profile=css3';
  document.getElementById("vLink1").setAttribute("href", HTMLvalidLinkStr);
  document.getElementById("vLink2").setAttribute("href", CSSvalidLinkStr);
}
window.onload = add_validation_links;
</script>
</head>
<body>
<h1>{{name}} in {{place}}</h1>

<main>
<p>
{{name}} was beginning to get very tired of sitting by her {{relation}} on the
bank, and of having nothing to do: once or twice she had peeped into the
{{thing}} her sister was {{action}}, but it had no pictures or conversations in
it, <q>and what is the use of a {{thing}},</q> thought {{name}} <q>without
pictures or conversation?</q>
</p>
<p>
So she was considering in her own {{organ}} (as well as she could, for the
{{adj1}} day made her feel very {{adj2}} and {{adj3}}), whether the pleasure of
making a {{thing2}}-chain would be worth the trouble of getting up and picking
the {{thing2}}s, when suddenly a White Rabbit with pink eyes ran close by her.
</p>
</main>

<footer>
<a id="vLink1">
<strong> HTML </strong> Valid! </a> | 
<a id="vLink2">
<strong> CSS </strong> Valid! </a>
</footer>

</body>
</html>
