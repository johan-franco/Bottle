from bottle import run, route, post, template, request


@route("/")
def start():
    return template("presentq")


@post("/q/")
def q():
    a = request.forms.get("number")
    b = request.forms.get("coe")
    return template("present", degree=int(a), coe=b)


@post("/p/<op>/<deg>/<coe>")
def polyget(op, deg, coe):
    a = []
    deg = int(deg)
    for i in range(len(coe)):
        a.append(deg-1)
    b = []
    c = []
    while a != [-1,]*len(coe):
        b.append(request.forms.get("p1" + str(a)))
        a[0] -= 1
        for i in range(len(a)):
            if a[i] == -1:
                if i == len(a) - 1:
                    break
                else:
                    a[i] = deg-1
                    a[i+1] -= 1
    while a != [-1,]*len(coe):
        c.append(request.forms.get("p2" + str(a)))
        a[0] -= 1
        for i in range(len(a)):
            if a[i] == -1:
                if i == len(a) - 1:
                    break
                else:
                    a[i] = deg-1
                    a[i+1] -= 1
    if op == "add" or op == "sub":
        for i in range(len(b)):
            if op == "add":
                b[i] += c[i]
            else:
                b[i] -= c[i]
    else:
        c = (deg ** 4) #maximum dimensions of polynomial
        for x in q:
            for y in q:
                if op == "div":
                    c = b[x] / c[y] #x / deg gives us the 1rst varible value, x % deg gives us the 2nd variable value, (x % deg) % deg gives us the 3rd, and etc.
                else:
                    c = b[x] * c[y]
    return template("answer", deg=deg, coe=coe, ans=b,)


run(server="gae")