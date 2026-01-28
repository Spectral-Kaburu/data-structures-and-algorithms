nums = [1,2,3]

# Figure out how to skip duplicates
class Backtrack:
    def __init__(self):
        pass

    def subsets(self, nums:list[int]):
        nums.sort()
        result = []

        def algo(index:int, path:list):
            if index == len(nums):
                print(f"End of subset, {path}")
                result.append(path[:]) # original, independent copy of path is formed
                return
            
            path.append(nums[index])
            algo(index+1, path)
            path.pop()

            algo(index+1, path)

        algo(0, [])
        return print(result)

tryout = Backtrack()
tryout.subsets(nums)
        
        
    