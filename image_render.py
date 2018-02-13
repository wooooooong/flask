from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/<imagename>/<size>/<imagename_size_zoom_x_y>')
def image_render(imagename, size, imagename_size_zoom_x_y):
    print (imagename_size_zoom_x_y)
    return send_from_directory(imagename +'/'+ size,
        imagename_size_zoom_x_y+'.jpg',
         as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
