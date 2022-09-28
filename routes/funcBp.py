from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions import db
from ..models.func import Func

funcBp = Blueprint('funcBp', __name__)

@funcBp.route('/func')
def funcAll():
    funcQuery = Func.query.all()
    return render_template('funcAll.html', funcs=funcQuery)

@funcBp.route('/func/update/<funcs.id>')
def funcUpdate(funcs.id=0):
    funcQuery = Func.query.filter_by(id = funcs.id).first()
    return render_template('funcUp.html', func=funcQuery) 

@funcBp.route('/func/upd', methods=["POST"])
def funcUpd():

    funcId = request.form["id"]
    funcFunc = request.form["func"]
    funcPlug = request.form["plug"]
    funcInput = request.form["inp"]
    funcOutput = request.form["outp"]
    funcDescrip = request.form["desc"]
    func = Func.query.filter_by(id = funcId).first()
    func.func = funcFunc
    func.plug = funcPlug
    func.inp = funcInput
    func.outp = funcOutput
    func.desc = funcDescrip
    db.session.add(func)
    db.session.commit()

    return redirect(url_for("funcBp.funcAll"))  

@funcBp.route('/func/new')
def funcNew():
    return render_template('funcAdd.html')

@funcBp.route('/func/add', methods=["POST"])
def funcAdd():

    funcFunc = request.form["func"]
    funcPlug = request.form["plug"]
    funcInput = request.form["inp"]
    funcOutput = request.form["outp"]
    funcDescrip = request.form["desc"]
    func = Func(func=funcFunc, plug=funcPlug, inp=funcInput, outp=funcOutput, desc=funcDescrip)
    db.session.add(func)
    db.session.commit()

    return redirect(url_for("funcBp.funcAll"))

@funcBp.route('/func/delete/<funcs.id>')
def funcDelete(funcs.id=0):
    funcQuery = Func.query.filter_by(id = funcs.id).first()
    return render_template('funcDel.html', func=funcQuery) 

@funcBp.route('/func/del', methods=["POST"])
def funcDel():

    funcId = request.form["id"]
    func = Func.query.filter_by(id = funcId).first()
    db.session.delete(func)
    db.session.commit()

    return redirect(url_for("funcBp.funcAll"))
  