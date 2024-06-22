#!/usr/bin/env python3
'''
This module implements a simple helper function
'''
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''
    This function calculates the start and end indexes for
    a given page and size

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page

    Returns:
        tuple: A tuple containing the start index and end index.
    '''
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        '''
        This function gets a page with the specified number of items
        ARGS:
            page (int) - page number
            page_size (int) - number of items per page
        '''
        assert isinstance(page, int) and page > 0, "page must be a\
        positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size\
        must be a positive integer"
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        This function implements hypermedia pagination
        ARGS:
            page (int) - page number
            page_size (int) - number of items per page
        '''
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        page_dataset = self.get_page(page, page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
                'page_size': len(page_dataset),
                "page": page,
                "data": page_dataset,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
