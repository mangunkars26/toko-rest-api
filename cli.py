import os
import click

# Base directories for controllers and models
CONTROLLER_DIR = './controllers'
MODEL_DIR = './models'

# Ensure directories exist
os.makedirs(CONTROLLER_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)


@click.group()
def cli():
    """Simple Flask CLI to create controllers and models."""
    pass


@cli.command()
@click.argument('controller_name')
@click.option('-m', '--model', is_flag=True, help='Create a model along with the controller')
def make_controller(controller_name, model):
    """Create a new controller file, and optionally a model."""
    controller_path = os.path.join(CONTROLLER_DIR, f'{controller_name.lower()}_controller.py')

    # Create controller file
    with open(controller_path, 'w') as f:
        f.write(f"""from flask import jsonify, request

def index():
    return jsonify({{"message": "{controller_name} index"}})

def show(id):
    return jsonify({{"message": "Show {controller_name} with id " + str(id)}})

def create():
    data = request.get_json()
    return jsonify({{"message": "{controller_name} created", "data": data}})

def update(id):
    data = request.get_json()
    return jsonify({{"message": "{controller_name} with id " + str(id) + " updated", "data": data}})

def delete(id):
    return jsonify({{"message": "{controller_name} with id " + str(id) + " deleted"}})
""")
    click.echo(f"Controller {controller_name} created at {controller_path}")

    # If --model flag is used, create a model file
    if model:
        model_name = controller_name.replace('Controller', '')
        model_path = os.path.join(MODEL_DIR, f'{model_name.lower()}.py')
        with open(model_path, 'w') as f:
            f.write(f"""from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class {model_name}(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    # Add other fields as needed
""")
        click.echo(f"Model {model_name} created at {model_path}")


if __name__ == '__main__':
    cli()
