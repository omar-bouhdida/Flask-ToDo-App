from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Boolean, default=False)

# Ensure database tables are created
with app.app_context():
    db.create_all()

# Home route - Display all todos
@app.route('/')
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)

# Add new todo
@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:  # Ensure title is not empty
        new_todo = Todo(title=title, complete=False)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('home'))

# Update todo status
@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:  # Ensure the todo exists
        todo.complete = not todo.complete
        db.session.commit()
    return redirect(url_for('home'))

# Delete a todo
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    if todo:  # Ensure the todo exists before deleting
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for('home'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)