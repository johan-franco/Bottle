<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>\\
%default = "URL Variables"
{{title if defined('title') else default}}</title>
<style type="text/css">
body {
    margin: 25px;
    padding: 25px;
}
main {
    border: 1px dotted #555;
    padding: 15px;
}
p {
    padding: 25px;
}
p.return {
    margin-bottom: -40px;
    text-align: center;
}
h1 {
    text-align: center;
}
blockquote {
    text-align: center;
    font-size: 3em;
    font-style: italic;
}
a, a:visited {
    color: #663;
    text-decoration: none;
}
footer {
    margin-top: 25px;
    text-align: center;
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

<main>
%include
</main>

<footer>
<a id="vLink1">
<strong> HTML </strong> Valid! </a> | 
<a id="vLink2">
<strong> CSS </strong> Valid! </a>
</footer>

</body>
</html>
