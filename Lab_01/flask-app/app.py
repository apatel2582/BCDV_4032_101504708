from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://media1.tenor.com/m/fAKIFrYkfpAAAAAd/sad-sad-cat.gif",
    "https://media.tenor.com/pFz1Q12_hXEAAAAM/cat-holding-head-cat.gif",
    "https://media.tenor.com/47qpxBq_Tw0AAAAM/cat-cat-meme.gif",
    "https://media.tenor.com/7t63GFnoIPUAAAAM/huh-cat-huh-m4rtin.gif",
    "https://media.tenor.com/Wyjcf1uN1AoAAAAM/cat-zoning-out-cat-stare.gif",
    "https://media.tenor.com/nqBUintQUbEAAAAM/cat.gif",
    "https://media.tenor.com/Jc9jT66AJRwAAAAM/chipi-chipi-chapa-chapa.gif",
    "https://media.tenor.com/7n0hNpCqS3kAAAAM/cat-driving-car.gif",
    "https://media.tenor.com/VfNHIfcyAIMAAAAM/watch-a-fat-cat-dance-an-american-dance-girlfriend.gif",
    "https://media.tenor.com/NQfq1liFH-8AAAAM/byuntear-sad.gif",
    "https://media.tenor.com/kRlG2TkDrBoAAAAM/cat-cat-meme.gif",
    "https://media.tenor.com/jmdUY9TVm5IAAAAM/cat-the-voices.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")