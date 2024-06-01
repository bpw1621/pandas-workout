import pytest

from pandas_workout.series.exam_scores import generate_exam_scores, HIGH, LOW, SIZE, average_exam_score, \
    first_half_average_exam_score, second_half_average_exam_score, second_half_improvement, did_improve_in_second_half


@pytest.fixture(params=[7, 177])
def rng_seed(request):
    return request.param


@pytest.fixture()
def exam_scores(rng_seed):
    return generate_exam_scores(rng_seed)


def test_exam_scores_length(exam_scores):
    assert len(exam_scores) == SIZE


def test_exam_scores_in_range(exam_scores):
    assert (LOW <= exam_scores).all() and (exam_scores <= HIGH).all()


def test_average_exam_score(exam_scores):
    assert exam_scores.min() <= average_exam_score(exam_scores) <= exam_scores.max()


def test_first_half_average_exam_score(exam_scores):
    exam_scores_min = exam_scores[:(SIZE // 2)].min()
    exam_scores_max = exam_scores[:(SIZE // 2)].max()
    assert exam_scores_min <= first_half_average_exam_score(exam_scores) <= exam_scores_max


def test_second_half_average_exam_score(exam_scores):
    exam_scores_min = exam_scores[(SIZE // 2):].min()
    exam_scores_max = exam_scores[(SIZE // 2):].max()
    assert exam_scores_min <= second_half_average_exam_score(exam_scores) <= exam_scores_max


def test_second_half_improvement(exam_scores, rng_seed):
    if rng_seed == 7:
        assert second_half_improvement(exam_scores) < 0
    else:
        assert second_half_improvement(exam_scores) > 0


def test_did_improve_in_second_half(exam_scores, rng_seed):
    if rng_seed == 7:
        assert not did_improve_in_second_half(exam_scores)
    else:
        assert did_improve_in_second_half(exam_scores)
