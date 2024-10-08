class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(array, low, high):
            pivot = array[high]
            i = low - 1
            for j in range(low, high):
                if array[j] < pivot:
                    i += 1
                    array[i], array[j] = array[j], array[i]
            array[i + 1], array[high] = array[high], array[i + 1]
            return i + 1
 
        def quickSort(array, low, high):
            if low < high:
                pi = partition(array, low, high)
                quickSort(array, low, pi - 1)
                quickSort(array, pi + 1, high)
        
        quickSort(nums, 0, len(nums) - 1)


'''
Quick sort
'''
