class Solution:
    def numberOfBeams(self, bank):
        # Step 1: Count devices ('1's) in each row
        device_counts = [row.count('1') for row in bank if row.count('1') > 0]
        
        # Step 2: Multiply adjacent non-empty rows
        beams = 0
        for i in range(1, len(device_counts)):
            beams += device_counts[i - 1] * device_counts[i]
        
        return beams
