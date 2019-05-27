#!/usr/bin/python2

import os, sys, json
import random
import string
import httplib2

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from flask import session as login_session

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker

from database_setup import Genre, Movies, Base


app = Flask(__name__)

# Create a connection to the database.
# avoiding the check for same thread. Gave a lot of errors when user refreshes.
engine = create_engine('sqlite:///moviegenre.db', connect_args={'check_same_thread':False}) # do not check for same thread.
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

################# show genre ########################
@app.route('/genres/')
def showGenres():
    """
    This method will dispaly all movie genres. They will be clickable.
    once the user clicks on this, it will display another page and it will show the actual movies.
    """
    genre = session.query(Genre).order_by(asc(Genre.name))
    return render_template('genre.html', genres=genre)

################# edit genre ########################
# Edit Genres.
@app.route('/genres/<int:genre_id>/edit/')
def editGenre(genre_id):
    """
    This method is responsible for making edits to the genre name.
    You can edit a specific Genre.
    """
    edit_genre = session.query(Genre).filter_by(id=genre_id).one()
    if request.method == 'POST':
        if request.form['name']:
            edit_genre = request.form['name']
            session.add(edit_genre)
            session.commit()
            flash("Movie Genre has been Edited.")
            return redirect(url_for("showGenres"))
    else:
        return render_template('editgenre.html', genre=edit_genre)


################# delete Genre ########################
# Delete Genre.
@app.route('/genres/<int:genre_id>/delete/', methods=['GET', 'POST'])
def deleteGenre(genre_id):
    """
    This method is responsible for deleting a particular Genre.
    The user will be asked for a confirmation before deleting.
    """

    # Getting the proper genre needed to delete by genre id.
    delete_genre = session.query(Genre).filter_by(id=genre_id).first()
    if request.method == 'POST': # this only happens if the method is post.
        session.delete(delete_genre)
        session.commit() # deleteing the Movie Genre.
        flash("you have successfully deleted the movie genre.") # prints out a message if anything has been modified.
        return redirect(url_for('showGenres', genre_id=genre_id)) # redirects to the main page.
    else:
        return render_template('delete.html', genre=delete_genre) # Displays the delete page.


################# Add new Genre ########################

# add new Movie Genre.
@app.route('/genres/new/', methods=['GET', 'POST'])
def newGenre():
    """
    User can creat a new Move Genere.
    The database will be updated and the list will be displayed on the homepage.
    """
    genre = Genre()
    if request.method == "POST":
        if request.form['name']:
            new_genre = request.form['name']
            session.add(Genre(name=new_genre))
            session.commit()
            flash("You Have created a new Genre.")
            return redirect(url_for('showGenres'))
    else:
        return render_template('newgenre.html')


################# shows movies. ########################
@app.route('/genres/<int:genre_id>/movies/')
def showMovies(genre_id):
    """This will display movies based on genres.
       this is connected via genre id. this is acting as foreign key in the movies table.
    """
    genre = session.query(Genre).filter_by(id=genre_id).one()
    movie = session.query(Movies).filter_by(genre_id=genre.id).all()

    return render_template('showmovies.html', movies=movie, genre=genre)


################# Add new Movie ########################
@app.route('/genres/<int:genre_id>/newmovie/', methods=['GET','POST'])
def addNewMovie(genre_id):
    """
    This will add new movies to a genre.
    """
    genre = session.query(Genre).filter_by(id=genre_id).one()

    if request.method == 'POST':
       new_movie = Movies(name=request.form['title'], 
                          description=request.form['description'],
                          year=request.form['date'], 
                          genre_id=genre_id)
       session.add(new_movie)
       session.commit()
       flash("New Movie added.")
       return redirect(url_for('showMovies', genre_id=genre_id))
    else:
       return render_template('newmovie.html', genre=genre)
       
################# Individualt Movie ########################
# Shows individual movie.
@app.route('/genres/<int:genre_id>/movies/<int:movie_id>/')
def movie(genre_id, movie_id):
    """
    This method is responsible for makeing edits to the
    movie title, description, and year.
    """
    genre = session.query(Genre).filter_by(id=genre_id).one()
    movie = session.query(Movies).filter_by(id=movie_id).one()
    return render_template('movie.html', movie=movie, genre=genre)

################# Edit Movie ########################
@app.route('/genres/<int:genre_id>/movies/<int:movie_id>/edit/', methods=['GET', 'POST'])
def editMovie(genre_id, movie_id):
    """
    Responsible for makeing edits to the selected movie. 
    Make edits to the name, year, and description.
    """
    genre = session.query(Genre).filter_by(id=genre_id).one()
    movie = session.query(Movies).filter_by(id=movie_id).one()
    
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        description = request.form['description']
        movie.name = title
        movie.year = year
        movie.description = description

        session.add(movie)
        session.commit()
        flash("You have edited a movie.")
        return redirect(url_for('showMovies', genre_id=genre_id))
    else:
        return render_template('editmovie.html', genre=genre, movie=movie)



if __name__ == '__main__':
    app.secret_key = 'secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)