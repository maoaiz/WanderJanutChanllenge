import datetime

from django.db import models
from django.utils import timezone


class Turn(models.Model):
    created_at = models.DateField()
    scheduled_for = models.DateField()
    is_same_day = models.BooleanField()

    @staticmethod
    def get_num_turns_by_date(date):
        return Turn.objects.filter(scheduled_for=date).count()

    @staticmethod
    def get_num_turns_added(initial_date, final_date):
        qs = Turn.objects.filter(scheduled_for__gte=initial_date, scheduled_for_lte=final_date)
        return qs.count()


def projected_sameday_turns(date):
    pass


def get_previous_range_dates(date):
    """
    Returns the initial and final date in the previous week of today.

    Ex. If today is a friday and date is a tuesday,
    the results are the last friday from today as initial_date and
    the last tuesday from today as final_date
    """

    today = timezone.now()

    today_dow = today.weekday()
    date_dow = date.weekday()

    if date_dow < today_dow:
        days = today_dow - date_dow
    else:
        days = 7 - date_dow + today_dow

    initial_date = today - datetime.timedelta(days=7)
    final_date = today - datetime.timedelta(days=days)

    return initial_date, final_date


def projected_turns(date):
    """
    Predict the number of turns for a date:

    Parameters:
    -----------
    date : datetime.date
        The date to predict the number of turns

    Returns:
    --------
    predicted_number : int
    """

    initial_date, final_date = get_previous_range_dates(date)

    num_weeks = 4
    turns_added_per_week = []

    # We iterate over last num_weeks to calculate the number of
    # turns scheduled every week
    for week in range(num_weeks):

        initial_date = initial_date - datetime.timedelta(days=week * 7)
        final_date = final_date - datetime.timedelta(days=week * 7)

        num_turns_added = Turn.get_num_turns_added(initial_date, final_date)
        turns_added_per_week.append(num_turns_added)

    # turns_added_per_week contains the number of turns scheduled per week
    total_avg_turns_added = sum(turns_added_per_week) / num_weeks

    turns_for_date = Turn.get_num_turns_by_date(date)

    predicted_number = int(total_avg_turns_added) + turns_for_date

    return predicted_number
