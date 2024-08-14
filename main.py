from fasthtml.common import *
from argumentChecker import *

app, rt = fast_app(live=True)


@rt('/')
def get():
    exp = P("Symbols: & | ! > @")
    frm = Form(Group(Input(placeholder="Ex: p > q | r , !(p > q) @ r", id='arg'),
                     Button("Enter")),
               hx_post='/', target_id='result'
               )
    result = P(None, id='result')
    return Titled("Argument Checker", exp, frm, result)


@rt('/')
def post(arg: str):
    result = argumentChecker(arg)
    if result == True:
        return P("Valid Argument", id='result')
    elif result == False:
        return P("Invalid Argument", id='result')
    elif result == 'Error':
        get()
        return result


serve()
