
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Page 1</title>
<style type="text/css">
body {
    margin: 25px;
    padding: 25px;
}
main {
    border: 1px dotted #555;
}
h1 {
    padding: 15px;
    text-align: center;
    font-size: 3em;
    font-weight: bold;
}
p {
    text-align: center;
    font-size: 1.5em;
}
a, a:visited {
    color: #663;
    text-decoration: none;
}
footer {
    margin-top: 5px;
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
<h1>Welcome To The Index Page</h1>

<a href= "template.tdl">Click to greet another page!</a>
<a href= "template.tdl">Go to the Main Stage! Kakavasha!</a>
</main>

<footer>
<a id="vLink1">
<strong> HTML </strong> Valid! </a> | 
<a id="vLink2">
<strong> CSS </strong> Valid! </a>
</footer>

</body>
</html>
