from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # debug mode is enabled and the default port is 127.0.0.1:5000