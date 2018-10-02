# find the tallest peak in the list
# iterate from both sides of the list towards tallest
#   track the max height seen and adding the volume of difference in height between max seen and current
def trapping_rain_water(heights):
    if len(heights) < 2:
        return 0
    
    # phase 1 - find index of tallest
    tallest_idx = None
    tallest_val = None
    for i in range(len(heights)):
        if not tallest_idx == None or heights[i] > tallest_val:
            tallest_idx = i
            tallest_val = heights[i]

    # phase 2 - start from both ends towards tallest
    running_sum = 0

    left_running_max = 0
    for i in range(0, tallest_idx):
        if heights[i] > left_running_max:
            left_running_max = heights[i]
        else:
            running_sum += left_running_max - heights[i]

    right_running_max = 0
    for i in reversed(range(tallest_idx, len(heights))):
        if heights[i] > right_running_max:
            right_running_max = heights[i]
        else:
            running_sum += right_running_max - heights[i]

    return running_sum


if __name__ == "__main__":
    heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trapping_rain_water(heights))
    assert trapping_rain_water(heights) == 6