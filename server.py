from wsgiref import headers
from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
def route_index():
    headers = data_handler.DATA_HEADER
    user_stories = data_handler.get_all_user_story()
    return render_template('index.html', headers=headers, user_stories=user_stories)


@app.route('/story', methods=['GET', 'POST'])
def add_user_story():
    if request.method == 'POST':
        data = dict(request.form)
        data['status'] = 'planning'
        data["id"] = data_handler.max_id() + 1
        data_handler.add_user_story(data)
        return redirect(url_for("route_index"))
    return render_template('story.html', story=None)


@app.route('/story/<id>', methods=['GET', 'POST'])
def edit_user_story(id):
    story = data_handler.get_user_story(id)
    if request.method == 'POST':
        data = dict(request.form)
        data_handler.update_user_story(data, id)
        return redirect(url_for("route_index"))
    return render_template('story.html', story=story)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
