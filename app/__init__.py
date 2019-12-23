from flask import Flask, render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__,
            static_url_path='', 
           
            )


from app import views

