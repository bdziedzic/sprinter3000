from flask import Flask, render_template, redirect, request
import data_manager
app = Flask(__name__)

story_id = 0
def new_id(story_id):
    story_id+=1
    return story_id


@app.route('/')
@app.route('/list')
def mainpage():
    return render_template('main.html')

@app.route('/story', methods=['POST'])
def newstory():
    return render_template('story.html')

@app.route('/story/<story_id>', methods=['POST'])
def storypage(story_id):
    return render_template('storypage.html')

if __name__ == "__main__":
    app.run(debug=True)