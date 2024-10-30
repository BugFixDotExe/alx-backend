#!/usr/bin/env python3
'''
A Python module or script
that conatins a function named index_range
that takes two integer arguments
page and page_size.
return a tuple
'''
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        ret_dataset = self.dataset()
        len_of_ret_dataset = len(ret_dataset)
        if page > len_of_ret_dataset or page_size > len_of_ret_dataset:
            return []
        start_page, end_page = index_range(page, page_size)
        if start_page > len_of_ret_dataset or end_page > len_of_ret_dataset:
            return []
        return ret_dataset[start_page: end_page]
