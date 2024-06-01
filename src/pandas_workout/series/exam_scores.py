# Create a series of 10 elements, random integers from 70 to 100, representing scores on a monthly exam. Set the index
# to be the month names, starting in September and ending in June. (If these months don’t match the school year in your
# location, feel free to make them more realistic.)
#
# With this series, write code to answer the following questions:
# - What is the student’s average test score for the entire year?
# - What is the student’s average test score during the first half of the year (i.e., the first five months)?
# - What is the student’s average test score during the second half of the year?
# - Did the student improve their performance in the second half? If so, by how much?
#
# Beyond the exercise
# - In which month did this student get their highest score? Note that there are at least three ways to accomplish this:
#   you can sort the values, taking the largest one, using a boolean (mask) index to find rows that match the value of
#   s.max(), the highest value, or invoking s.idxmax(), which returns the index of the highest value.
# - What were this student’s five highest scores?
# - Round the student’s scores to the nearest 10. (A score of 82 would be rounded down to 80, but a score of 87 would be
#   rounded up to 90.) Be sure to read the documentation for the round method (http://mng.bz/8rzg) to understand its
#   arguments and how it handles numbers like 15 and 75.

import calendar

import numpy as np
import pandas as pd

HIGH = 100
LOW = 70
SIZE = 10


def generate_exam_scores(rng_seed: int, low: int = LOW, high: int = HIGH, size: int = SIZE) -> pd.Series:
    random_generator = np.random.default_rng(rng_seed)
    index = list(calendar.month_name)[9:] + list(calendar.month_name)[1:7]
    return pd.Series(random_generator.integers(low=low, high=high, size=size), index=index)


def average_exam_score(exam_scores: pd.Series) -> float:
    return exam_scores.mean()


def first_half_average_exam_score(exam_scores: pd.Series) -> float:
    return average_exam_score(exam_scores[:(SIZE // 2)])


def second_half_average_exam_score(exam_scores: pd.Series) -> float:
    return average_exam_score(exam_scores[(SIZE // 2):])


def second_half_improvement(exam_scores: pd.Series) -> float:
    return second_half_average_exam_score(exam_scores) - first_half_average_exam_score(exam_scores)


def did_improve_in_second_half(exam_scores: pd.Series) -> bool:
    return second_half_improvement(exam_scores) > 0
