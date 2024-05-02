<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style type="text/css">
html {
  background-color: #FFD;
}
div {
  border-radius: 25px;
  border: 1px solid #888;
  padding-left: 15px;
  background-color: #DDE;
  text-align: left;
}
body {
  text-align: center;
}
</style>
<title>Polynomial Calculator</title>
</head>
<body>
<div>
<form name="#" action="/q/" method="post">
Degree of Polynomial: <input name="number" type="text" value="{{degree}}"> Different Variables(no spaces): <input name="coe" type="text" value="{{coe}}">
<input name="submit#" type="submit" value="Update Degree and Variables">
</form>
%deg = degree
%zoe = coe[::-1]
<hr>First Polynomial:<br>
<form id="poly" method="post">
%a = []
%for i in range(len(coe)):
%    a.append(deg)
%end
%f = True
%while f:
    <input type="text" id="p1{{a}}" size="1" value={{}}>
%    b = range(len(a))
%    b.reverse()
%    for i in b:
%        if a[i] != 0:
%            if a[i] == 1:
                {{zoe[i]}}
%            else:
                {{zoe[i]}}
                <sup>
                {{a[i]}}
                </sup>
%            end
%        end
%    end
%    a[0] -= 1
%    for i in range(len(a)):
%        if a[i] == -1:
%            if i == len(a) - 1:
%                f = False
%            else:
%                a[i] = deg
%                a[i+1] -= 1
%            end
%        end
%    end
%    if f:
        &nbsp;+&nbsp;
%    end
%end
<hr>Second Polynomial:<br>
%a = []
%for i in range(len(coe)):
%    a.append(deg)
%end
%f = True
%while f:
    <input type="text" id="p2{{a}}" size="1">
%    b = range(len(a))
%    b.reverse()
%    for i in b:
%        if a[i] != 0:
%            if a[i] == 1:
                {{zoe[i]}}
%            else:
                {{zoe[i]}}
                <sup>
                {{a[i]}}
                </sup>
%            end
%        end
%    end
%    a[0] -= 1
%    for i in range(len(a)):
%        if a[i] == -1:
%            if i == len(a) - 1:
%                f = False
%            else:
%                a[i] = deg
%                a[i+1] -= 1
%            end
%        end
%    end
%    if f:
        &nbsp;+&nbsp;
%    end
%end
<br><button form="poly" formaction="/p/add/{{degree}}/{{coe}}">Add</button>
<button form="poly" formaction="/p/sub/{{degree}}/{{coe}}">Subtract</button>
<button form="poly" formaction="/p/mul/{{degree}}/{{coe}}">Multiply</button>
<button form="poly" formaction="/p/div/{{degree}}/{{coe}}">Divide</button>
</form>
<br>
</div>
<footer>
<a href="http://validator.w3.org/check/referer">
<strong> HTML </strong> Valid! </a>
<a href="http://jigsaw.w3.org/css-validator/check/referer?profile=css3">
<strong> CSS </strong> Valid! </a>
</footer>
</body></html>
