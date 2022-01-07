# def isRectangleOverlap(rec1: list, rec2: list):
#     return rec1[0] < rec2[2] and rec1[2] > rec2[0] and rec1[1] < rec2[3] and rec1[3] > rec2[1]

def doOverlap(L1, R1, L2, R2):
    if(L1[0] > R2[0] or L1[1] < R2[1] or L2[0] > R1[0] or L2[1] < R1[1]):
        return 0
    return 1

# print(doOverlap([0, 2],[1, 1],[-2, 0],[0, -3]))
# print(doOverlap([0, 10],[10, 0],[5, 5],[15, 0]))
