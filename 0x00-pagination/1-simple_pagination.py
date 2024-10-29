#!/usr/bin/env python3
"""
A method named get_page that takes two integer
arguments page with default value 1 and page_size
with default value 10.

You have to use this CSV file (same as the one presented
at the top of the project)
Use assert to verify that both arguments are integers
greater than 0. Use index_range to find the correct
indexes to paginate the dataset correctly and return the
appropriate page of the dataset (i.e. the correct list of rows).
If the input arguments are out of range for the dataset,
an empty list should be returned.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index from a particular page and page size"""
    # if page is 1, start at 0 and end at page_size
    # if page is 2, start at ((page-1) * page_size) and
    # end at (page_size * page)
    # if page is 3, start at ((page-1) * page_size) and
    # end at (page_size * page)
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        # get data from the csv file
        data = self.dataset()

        try:
            # Retrieve the index to the start and end of data
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []
