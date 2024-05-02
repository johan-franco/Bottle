<h1>Please enter {{source}} to be changed to {{target}} below:</h1>

<h2>{{helptext}}</h2>

<p>Enter {{source}} here!</p>
<form action="{{sourcepage}}" method="GET">
<textarea name="Translater" cols="175" rows="5"></textarea>
<input type="submit" name="save" value="submit">
</form>

<p class="displayer">{{display}}</p>
<p class="linker">
<a href = "{{targetpage}}">Click here to go to the {{target}} translater</a>
</p>
<p class="linker">
<a href = "/">Click to go back to the main page</a>
</p>

%rebase views/layout
