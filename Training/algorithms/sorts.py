# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:54:54 2021

@author: Vladimir
"""


class SortAlgorithms(object):
    def __init__(self):
        self.sort_array = [5, 3, 1, 4, 2, 6, 8, 9, 7]
        
    def __str__(self):
        return str(
            f"Bubble sort:     { self.bubble_sort(self.sort_array.copy())} \tBig-O: O(n^2)\n"
            f"Selection sort:  { self.selection_sort(self.sort_array.copy())} \tBig-O: O(n^2)\n"
            f"Insertion sort:  { self.insertion_sort(self.sort_array.copy())} \tBig-O: O(n^2)\n"
            )
    
    # BUBBLE SORT -> compare every element of array while the next element     
    # is larger than current and swipe them
    @staticmethod
    def bubble_sort(array):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(array) - 1):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True
        return array

    # SELECTION SORT -> find smallest element in tail of array and switch it with
    # head of array, than proceed to first element of tail
    @staticmethod
    def selection_sort(array):
        for i in range(len(array)):
            lowest_value_index = i
            for j in range(i + 1, len(array)):
                if array[j] < array[lowest_value_index]:
                    lowest_value_index = j
            array[i], array[lowest_value_index] = array[lowest_value_index], array[i]
        return array
    
    # INSERTION SORT ->  
    # 
    def insertion_sort(self, array):
        return array


if __name__ == "__main__":
    print(SortAlgorithms())