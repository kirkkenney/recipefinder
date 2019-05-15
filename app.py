from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import os


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/', methods=['GET'])
def home():
    conn = sqlite3.connect('recipes.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS recipes (id INTEGER PRIMARY KEY, img TEXT, title TEXT, description TEXT, timetocook TEXT, ingredients TEXT, instructions TEXT)")
    conn.commit()
    cur.execute("SELECT * FROM recipes")
    recipe_list = cur.fetchall()
    img_files, titles, descs, times, ids = [], [], [], [], []
    for card in recipe_list:
        ids.append(card[0])
        img_files.append(card[1])
        titles.append(card[2])
        descs.append(card[3])
        times.append(card[4])
    return render_template('index.html', zip=zip(ids, img_files, titles, descs, times))


@app.route('/add-recipe', methods=['POST', 'GET'])
def add_form():
    return render_template('add_recipe.html')


@app.route('/', methods=['POST'])
def add_recipe():
    if request.method == 'GET':
        return redirect(url_for('home'))
    target = os.path.join(APP_ROOT, 'static\\images\\')
    recipe_title = request.form.get('recipe_title')
    recipe_desc = request.form.get('recipe_description')
    recipe_time = request.form.get('recipe_time')
    recipe_ingredients = request.form.get('recipe_ingredients')
    recipe_instructions = request.form.get('recipe_instructions')
    file = request.files['img_file']
    filename = file.filename
    destination = "\\".join([target, filename])
    file.save(destination)
    conn = sqlite3.connect('recipes.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO recipes VALUES (NULL, ?, ?, ?, ?, ?, ?)", (filename, recipe_title, recipe_desc, recipe_time, recipe_ingredients, recipe_instructions,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

@app.route('/recipe-details', methods=["POST"])
def recipe_details():
    recipe = request.form.get('recipe_id')
    conn = sqlite3.connect('recipes.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM recipes WHERE id=?", (int(recipe),))
    results = cur.fetchall()
    img = results[0][1]
    title = results[0][2]
    description = results[0][3]
    time = results[0][4]
    ingredients = results[0][5]
    instructions = results[0][6]
    instructions_list = instructions.split('\r')
    ingredients_list = ingredients.split('\r')
    return render_template('recipe_details.html', img=img, title=title,
        description=description, time=time, ingredients_list=ingredients_list,
        instructions_list=instructions_list)


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
