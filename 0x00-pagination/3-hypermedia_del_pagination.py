#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializing a new Server instance"""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[i] for i in range(len(dataset))
                    }
            return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves the info about a page from a given index and with
        a specific size
        """
        data = self.indexed_dataset()
        page_data = []  # collect all index data in a dictionary
        count = 0
        next_index = None
        start = index if index else 0

        # validate index
        assert isinstance(index, int)
        assert index is not None and 0 <= index <= max(data.keys())
        assert isinstance(page_size, int) and page_size > 0

        for count, val in data.items():
            if count >= start and count < page_size:
                page_data.append(val)
                count += 1
                continue
            if count == page_size:
                next_index = count
                break
        page_info = {
                'index': index,
                'data': page_data,
                'page_size': len(page_data),
                'next_index': next_index,
        }
        return page_info
