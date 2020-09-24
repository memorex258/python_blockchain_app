from app import app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
else:
    app.run(debug=True, host='0.0.0.0')
