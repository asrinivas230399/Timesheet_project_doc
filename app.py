from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/projects/add', methods=['GET'])
def render_add_project_page():
    # Render the Projects Add Page
    return render_template('add_project.html')

@app.route('/projects/add', methods=['POST'])
def handle_add_project_submission():
    # Handle form submission
    project_name = request.form.get('project_name')
    project_description = request.form.get('project_description')
    
    # Here you would typically add logic to save the project to a database
    # For now, we'll just print the values to the console
    print(f"Project Name: {project_name}")
    print(f"Project Description: {project_description}")
    
    # Emit a WebSocket event for real-time updates
    socketio.emit('project_added', {
        'project_name': project_name,
        'project_description': project_description
    })
    
    # Redirect to a different page after successful submission
    return redirect(url_for('render_add_project_page'))

if __name__ == '__main__':
    socketio.run(app, debug=True)
