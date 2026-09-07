class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 :
            return 0 if nums[0] == target else -1
        
        leftPointer = 0
        rightPointer = len(nums)-1

        while leftPointer <= rightPointer :
            mid = (leftPointer + rightPointer)//2
            print(leftPointer,mid,rightPointer)

            if nums[leftPointer] == target :
                return leftPointer
            elif nums[rightPointer] == target :
                return rightPointer
            elif nums[mid] == target :
                return mid
            elif nums[mid] < nums[rightPointer] :
                if nums[mid] < target and nums[rightPointer] > target :
                    leftPointer = mid + 1
                else :
                    rightPointer = mid - 1
            elif nums[mid] > nums[leftPointer] :
                if  nums[mid] > target and nums[leftPointer] < target :
                    rightPointer = mid - 1
                else :
                    leftPointer = mid + 1
            else :
                rightPointer = mid - 1

        return -1
        