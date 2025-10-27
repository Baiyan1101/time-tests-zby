import pytest
import times


def test_given_input():
    # Arrange
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = times.compute_overlap_time(large, short)
    expected = [
        ("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
        ("2010-01-12 10:38:00", "2010-01-12 10:45:00"),
    ]
    assert result == expected

def test_no_overlap():
    # Arrange
    range1 = times.time_range("2022-01-01 08:00:00", "2022-01-01 09:00:00")
    range2 = times.time_range("2022-01-01 10:00:00", "2022-01-01 11:00:00")
    result = times.compute_overlap_time(range1, range2)
    expected = []
    
    assert result == expected

def test_time_range_in_order():
    start_time = "2022-01-01 10:00:00"
    end_time = "2022-01-01 09:00:00"

    with pytest.raises(ValueError, match="start_time must be less than or equal to end_time"):
        times.time_range(start_time, end_time)