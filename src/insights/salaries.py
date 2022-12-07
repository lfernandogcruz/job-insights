from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    base_file = read(path)
    return max([int(job["max_salary"]) for job in base_file
                if (job["max_salary"]).isdigit()])
    raise NotImplementedError
# big shout out to instructor Maria Carolina and her brilliant
# mentorship with the pokemon's get_max_attack example


def get_min_salary(path: str) -> int:
    base_file = read(path)
    return min([int(job["min_salary"]) for job in base_file
                if (job["min_salary"]).isdigit()])
    raise NotImplementedError
# big shout out to instructor Maria Carolina and her brilliant
# mentorship with the pokemon's get_min_attack example


def job_salaries_validation(job: Dict) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        return False
    if not int(job["min_salary"]):
        return False
    if not int(job["max_salary"]):
        return False
    if int(job["min_salary"]) > int(job["max_salary"]):
        return False
    return True


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if not job_salaries_validation(job):
        raise ValueError
    if not int(salary):
        raise ValueError
    if int(salary) <= 0:
        raise ValueError
    if (
        int(job["min_salary"]) <= int(salary)
        and int(salary) <= int(job["max_salary"])
    ):
        return True
    return False
    raise NotImplementedError
    # to test it run:
    # python3 -m pytest -k test_matches_salary_range


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    filtered_jobs = []
    for job in jobs:
        if matches_salary_range(job, salary):
            filtered_jobs.append(job)
    return filtered_jobs
    raise NotImplementedError
