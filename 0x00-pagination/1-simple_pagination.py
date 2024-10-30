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
    '''
    index_range: A function that computes the index range
    Args:
        page: the page
        page_size: the page size
    Returns:
        A tuples containg the start and end page numbers
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        '''
        The consturcutor of the class
        '''
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
        get_page: A function that retireves the content of the CSV
        Args:
            page(int): the start page
            page_size(int): the amout of content of the page
        Returns:
            A list containg the list of of matching computed page and page size
        '''
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
