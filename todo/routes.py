from flask import current_app as app
from flask import render_template, redirect, url_for
from todo import db
from .model.todo import Todo
from .forms import TodoForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = Todo(title=form.title.data)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('index'))
    todos = Todo.query.all()
    return render_template('index.html', form=form, todos=todos)


@app.route('/complete/<int:todo_id>')
def todo_complete(todo_id):
    todo = Todo.query.get(todo_id)
    todo.complete = True
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>')
def todo_delete(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))
