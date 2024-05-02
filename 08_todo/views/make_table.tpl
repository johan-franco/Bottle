<h2>{{heading}}</h2>
<table>
%for row in rows:
<tr>
  %for col in row:
    <td>{{col}}</td>
  %end
</tr>
%end
</table>

%rebase layout
