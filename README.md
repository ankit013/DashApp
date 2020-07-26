# DASH - Plotly

Dash is a productive Python framework for building web applications.Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It's particularly suited for anyone who works with data in Python.
Through a couple of simple patterns, Dash abstracts away all of the technologies and protocols that are required to build an interactive web-based application. Dash is simple enough that you can bind a user interface around your Python code in an afternoon.
Dash apps are rendered in the web browser. You can deploy your apps to servers and then share them through URLs. Since Dash apps are viewed in the web browser, Dash is inherently cross-platform and mobile ready.

## Dash App Gallery

https://dash-gallery.plotly.host/Portal/


## Dash Installation

pip install dash==1.13.3

https://dash.plotly.com/installation

## Dash Components

1. Dash html component : https://dash.plotly.com/dash-html-components
2. Dash core component : https://dash.plotly.com/dash-core-components
3. Dash data table : https://dash.plotly.com/datatable

## Dash application deployment using Heroku

The deployment process using Heroku is relatively easy. Check out this guide for deploying to Heroku.

1. To begin, you need to create a Heroku account.
2. Define a requirements.txt file with the packages to run your Dash app and python files.
3. Define a Procfile (a text in the root directory of your repo) to specify the command to start your app.

   **web: gunicorn app:server**
   
4. Specify your github repo and branch for deployment. You can do this using the heroku CLI or their web interface.
5. Deploy!
