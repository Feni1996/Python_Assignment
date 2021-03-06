"""Create a class to find three elements that sum to zero from a set of n real numbers
Input array: [-25,-10,-7,-3,2,4,8,10]
Expected output: [[-10,2,8],[-7,-3,10]]"""

class Task3:
 def triple(self, nums):
        nums= sorted(nums)
        result = []
        found = False
        for i in range(0, len(nums)-2):
        
            for j in range(i+1, len(nums)-1):
            
                for k in range(j+1, len(nums)):
                
                    if (nums[i] + nums[j] + nums[k] == 0):
                        result.append([nums[i], nums[j], nums[k]])
                        found = True
        return result

        if (found == False):
            print(" not exist ")
       

print(Task3().triple([-25, -10, -7, -3, 2, 4, 8, 10]))