from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    mock_jobs = [
        {"min_salary": 182, "max_salary": 238, "date_posted": "2022-01-18"},
        {"min_salary": 3000, "max_salary": 3500, "date_posted": "2019-11-23"},
        {"min_salary": 2000, "max_salary": 30000, "date_posted": "2017-03-07"},
    ]

    sorted_by_min_salary = [
        {"min_salary": 182, "max_salary": 238, "date_posted": "2022-01-18"},
        {"min_salary": 2000, "max_salary": 30000, "date_posted": "2017-03-07"},
        {"min_salary": 3000, "max_salary": 3500, "date_posted": "2019-11-23"},
    ]

    sorted_by_max_salary = [
        {"min_salary": 2000, "max_salary": 30000, "date_posted": "2017-03-07"},
        {"min_salary": 3000, "max_salary": 3500, "date_posted": "2019-11-23"},
        {"min_salary": 182, "max_salary": 238, "date_posted": "2022-01-18"},
    ]

    sorted_by_date_posted = [
        {"min_salary": 182, "max_salary": 238, "date_posted": "2022-01-18"},
        {"min_salary": 3000, "max_salary": 3500, "date_posted": "2019-11-23"},
        {"min_salary": 2000, "max_salary": 30000, "date_posted": "2017-03-07"},
    ]

    sort_by(mock_jobs, "min_salary")
    assert mock_jobs == sorted_by_min_salary

    sort_by(mock_jobs, "max_salary")
    assert mock_jobs == sorted_by_max_salary

    sort_by(mock_jobs, "date_posted")
    assert mock_jobs == sorted_by_date_posted
