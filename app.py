from flask import Flask, render_template
import templates

flask_app = Flask(__name__, template_folder="templates")
