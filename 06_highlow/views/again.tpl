
<h2>{{message}}</h2>
<form method="post" action="/">
  <label>Guess again: <input name="guess" type="text"></label>
  <button type="submit">Submit</button>
</form>

<h2>Guess count is now: <span>{{guesscount}}</span></h2>

%rebase layout
