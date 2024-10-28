#!/usr/bin/env python3
'''Task 1: Simple pagination'''
import csv
import math
from typing import List, Mapping
index_range = __import__('0-simple_helper_function').index_range


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
        '''Returns appropriate page of db'''
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        pages = index_range(page, page_size)
        try:
            db = self.dataset()
            return db[pages[0]:pages[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Mapping:
        '''returns a dictionary containing the following key-value pairs:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer'''
        hyper_dict = {
                'page_size': page_size,
                'page': page,
                'dataset': self.get_page(page, page_size),
                'total_pages': len(self.dataset())
                }
        start, end = index_range(page, page_size)
        hyper_dict['next_page'] = page + 1 \
            if end < hyper_dict['total_pages'] else None
        hyper_dict['prev_page'] = page - 1 if start > 0 else None
        return hyper_dict
