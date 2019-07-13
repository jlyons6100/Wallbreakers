class Solution:
    # Got a hint from thinking about ranges of values.
    def partitionLabels(self, S: str) -> List[int]:
        ind_in_arr = {}
        arr = []
        count = 0
        # Create ranges for value locations in string
        for ind in range(len(S)):
            ltr = S[ind]
            if not ltr in ind_in_arr:
                arr.append([ind, ind])
                ind_in_arr[ltr] = count
                count += 1
            else:
                arr[ind_in_arr[ltr]][1] = ind
        val2 = arr[0][1]  
        val1 = arr[0][0]
        ret = []
        for ind in range(len(arr)):
            # Keep track of initial range
            # If new range is inside current do nothing
            # If new range begins inside current range and goes out of it, expand current range
            # Else if the new range starts outside of the current range, start a new range
            if val2 > arr[ind][0] and val2 < arr[ind][1]:
                val2 = arr[ind][1]
            elif val2 < arr[ind][0]:
                ret.append(val2 - val1 + 1)
                val2 = arr[ind][1]
                val1 = arr[ind][0]
        if [val1, val2] not in ret:
            ret.append(val2 - val1 + 1)
        return ret
        
            