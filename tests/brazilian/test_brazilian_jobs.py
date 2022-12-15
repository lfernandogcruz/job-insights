from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    brazuka_file = read_brazilian_file("tests/mocks/brazilians_jobs.csv")

    for trampo in brazuka_file:
        assert "title" in trampo
        assert "salary" in trampo
        assert "type" in trampo
