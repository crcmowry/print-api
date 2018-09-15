# Defines the main flask app behind the print api
from flask import Flask

app = Flask(__name__)

# Landing/upload page
import api.index
# Print endpoint
import api.printfile
