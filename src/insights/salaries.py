from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    base_file = read(path)
    return max(
        [
            int(job["max_salary"])
            for job in base_file
            if (job["max_salary"]).isdigit()
        ]
    )


# big shout out to instructor Maria Carolina and her brilliant
# mentorship with the pokemon's get_max_attack example


def get_min_salary(path: str) -> int:
    base_file = read(path)
    return min(
        [
            int(job["min_salary"])
            for job in base_file
            if (job["min_salary"]).isdigit()
        ]
    )


# big shout out to instructor Maria Carolina and her brilliant
# mentorship with the pokemon's get_min_attack example


def job_salaries_validation1(job: Dict) -> bool:
    if "min_salary" not in job or "max_salary" not in job:
        return False
    if job["min_salary"] is None or job["max_salary"] is None:
        return False
    return True


def job_salaries_validation2(job: Dict) -> bool:
    try:
        if (not int(job["min_salary"]) or int(job["min_salary"]) < 0) and int(
            job["min_salary"]
        ) != 0:
            return False
        if (not int(job["max_salary"]) or int(job["max_salary"]) < 0) and int(
            job["max_salary"]
        ) != 0:
            return False
        return True
    except (TypeError, KeyError):
        return False


def job_salaries_validation3(job: Dict) -> bool:
    try:
        if int(job["min_salary"]) > int(job["max_salary"]):
            return False
        return True
    except (TypeError, KeyError):
        return False


def salary_check(salary: Union[int, str]) -> bool:
    try:
        if salary is None:
            return False
        if salary == 0:
            return True
        salary = int(salary)
        # if not int(salary):
        #     return False
        return True
    except (ValueError, TypeError, KeyError):
        return False


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    is_range_valid1 = job_salaries_validation1(job)
    is_range_valid2 = job_salaries_validation2(job)
    is_range_valid3 = job_salaries_validation3(job)
    is_salary_valid = salary_check(salary)
    if not (
        is_range_valid1
        and is_range_valid2
        and is_range_valid3
        and is_salary_valid
    ):
        raise ValueError
    if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
        return True
    return False


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)

        except ValueError:
            pass
    return filtered_jobs


# big shout out to instructor Rodrigo Coin Curvo and his brilliant
# insights and overview of this code.
# Not only guided me trough the code and helped me understand
# the logic behind it, but also made sure to suport me even with
# my connection breaking down in the middle of the mentoring session
# multiple times.
