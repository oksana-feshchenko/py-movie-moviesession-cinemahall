import datetime
from django.db.models import QuerySet

from db.models import MovieSession, Movie, CinemaHall


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int) -> None:
    new_hall = CinemaHall.objects.get(id=cinema_hall_id)
    new_movie = Movie.objects.get(id=movie_id)
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=new_hall,
        movie=new_movie
    )


def get_movies_sessions(session_date: str = None) -> QuerySet:
    sessions = MovieSession.objects.all()
    if session_date:
        sessions = sessions.filter(
            show_time__date=session_date)
    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    sessions = MovieSession.objects.all()
    session = sessions.get(id=movie_session_id)
    return session


def update_movie_session(session_id: int,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None
                         ) -> None:
    movie_session = MovieSession.objects.filter(id=session_id)
    if show_time:
        movie_session.update(show_time=show_time)
    if movie_id:
        new_movie = Movie.objects.get(id=movie_id)
        movie_session.update(movie=new_movie)
    if cinema_hall_id:
        new_hall = CinemaHall.objects.get(id=cinema_hall_id)
        movie_session.update(cinema_hall=new_hall)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()