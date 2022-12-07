from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    base_file = read(path)
    industries = []
    for job in base_file:
        if job["industry"] not in industries:
            if job["industry"] != "":
                industries.append(job["industry"])
    return industries
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_jobs = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_jobs.append(job)
    return filtered_jobs
    raise NotImplementedError
