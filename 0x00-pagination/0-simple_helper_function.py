#!/usr/bin/env python3
"""
A function named index_range that takes two integer
arguments page and page_size.
The function returns a tuple of size two containing
a start index and an end index corresponding to the
range of indexes to return in a list for those
particular pagination parameters.
Page numbers are 1-indexed, i.e. the first page is page 1.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """retrieve the index range of particular page and page size"""
    # if page is 1, start at 0 and end at page_size
    # if page is 2, start at ((page-1) * page_size) and
    # end at (page_size * page)
    # if page is 3, start at ((page-1) * page_size) and
    # end at (page_size * page)
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
