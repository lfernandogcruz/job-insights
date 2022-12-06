from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as read_file:
        reader = csv.DictReader(read_file, delimiter=",", quotechar='"')
        return list(reader)
    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    base_file = read(path)
    job_types = []
    for job in base_file:
        if job["job_type"] not in job_types:
            job_types.append(job["job_type"])
    return job_types
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs.append(job)
    return filtered_jobs
    raise NotImplementedError
