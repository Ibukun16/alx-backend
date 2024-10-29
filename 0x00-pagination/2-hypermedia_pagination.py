#!/usr/bin/env python3
"""
Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary containing
the following key-value pairs:

page_size: the length of the returned dataset page
page: the current page number
data: the dataset page (equivalent to return from previous task)
next_page: number of the next page, None if no next page
prev_page: number of the previous page, None if no previous page
total_pages: the total number of pages in the dataset as an integer
Make sure to reuse get_page in your implementation.
"""
import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a particular page and page size"""
    # if page is 1, start at 0 and end at page_size
    # if page is 2, start at ((page-1) * page_size) and
    # end at (page_size * page)
    # if page is 3, start at ((page-1) * page_size) and
    # end at (page_size * page)

    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
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

        # get the data from the csv
        data = self.dataset()

        try:
            # get the index to start and end
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieve information about a page in a a dictionary
        containing the key value pairs as below:
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        start, end = index_range(page, page_size)

        # estimating the next page
        if (page < total_pages):
            next_page = page + 1
        else:
            next_page = None

        # estimating previous page
        if (page == 1):
            prev_page = None
        else:
            prev_page = page - 1

        page_details = {
                'page_size': len(page_data),
                'page': page,
                'data': page_data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages,
        }
        return page_details
