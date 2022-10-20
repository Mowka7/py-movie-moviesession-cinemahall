from django.db.models import QuerySet, DateTimeField
from db.models import MovieSession


def create_movie_session(
        movie_show_time: DateTimeField,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )


def get_movies_sessions(session_date: DateTimeField = None) -> QuerySet:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> QuerySet:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: DateTimeField = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:

    queryset = MovieSession.objects.get(id=session_id)
    if show_time:
        queryset.show_time = show_time
    if movie_id:
        queryset.movie_id = movie_id
    if cinema_hall_id:
        queryset.cinema_hall_id = cinema_hall_id
    queryset.save()

    return queryset


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.get(id=session_id).delete()