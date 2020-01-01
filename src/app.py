from flask import Flask, render_template,send_from_directory,request
# from GradeScraper import scrapeforgrades
app = Flask(__name__, template_folder= "/templates")


@app.route("/")
def index():
        #return("Index str")
    return render_template("index.html")


@app.route('/robots.txt')
@app.route('/AI_list.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)