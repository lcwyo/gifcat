from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr01/15/9/anigif_enhanced-buzz-31540-1381844535-8.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26388-1381844103-11.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr05/15/9/anigif_enhanced-buzz-26390-1381844163-18.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr06/15/10/anigif_enhanced-buzz-1376-1381846217-0.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr06/15/10/anigif_enhanced-buzz-29111-1381845968-0.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr03/15/9/anigif_enhanced-buzz-3409-1381844582-13.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr06/15/9/anigif_enhanced-buzz-23859-1381845509-0.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr03/15/10/anigif_enhanced-buzz-11980-1381846269-1.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2013-10/enhanced/webdr01/15/10/anigif_enhanced-buzz-27208-1381845845-0.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/11/enhanced/webdr11/anigif_enhanced-19791-1446482500-3.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/12/enhanced/webdr12/anigif_enhanced-1659-1446484096-3.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2015-11/2/12/enhanced/webdr07/anigif_enhanced-21011-1446486948-2.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
