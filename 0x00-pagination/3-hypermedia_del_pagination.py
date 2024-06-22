#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None
        self.deleted_indices = set()

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
        '''
        Implementing a deletion resilient hypermedia pagination
        '''
        if index is None:
            index = 0

        assert 0 <= index < len(self.dataset()), "Index out of range"
        data = []
        next_index = index
        current_size = 0

        while current_size < page_size and next_index < len(self.dataset()):
            if next_index not in self.deleted_indices:
                data.append(self.dataset()[next_index])
                current_size += 1
            next_index += 1

        return {
                "index": index,
                "next_index": next_index,
                "page_size": len(data),
                "data": data
        }
