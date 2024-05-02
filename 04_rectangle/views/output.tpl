<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Rectangle Area and Perimeter</title>
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
    padding: 40px;
}
main p {
    padding: 10px;
}
a, a:visited {
    color: #663;
    text-decoration: none;
}
div#rect {
    width: {{length}}vw;
    height: {{width}}vw;
    background-color: {{color}};
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
<h1>Rectangle Area and Perimeter</h1>

<main>
<h2>A {{color.capitalize()}} {{width}} by {{length}} Rectangle</h2>
<div id="rect"></div>

<h2>About This Rectangle</h2>
<p>
This {{color}} rectangle has a perimeter of {{perimeter}} screen units and an
area of {{area}} screen units.
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
