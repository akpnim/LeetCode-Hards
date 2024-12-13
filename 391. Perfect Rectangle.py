import math
class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        #step 1: lets get all the points from rectangles and put it back into rectangels 
        #in the form [[LL],[UL],[UR],[LR]]
        all_points = []
        for rec in rectangles:
            all_points.append([rec[0],rec[1]]) #LL point 
            all_points.append([rec[0],rec[3]]) #UL point 
            all_points.append([rec[2],rec[3]]) #UR point 
            all_points.append([rec[2],rec[1]]) #LR point 
        #step2: lets find the global LL, UL, UR, LR points 
        max_x, max_y, min_x, min_y = -math.inf, -math.inf, math.inf, math.inf 
        for point in all_points:
            if point[0] > max_x:
                max_x = point[0]
            if point[0] < min_x: 
                min_x = point[0]
            if point[1] > max_y: 
                max_y = point[1]
            if point[1] < min_y: 
                min_y = point[1]
        
        LL = (min_x, min_y)
        UL = (min_x, max_y)
        UR = (max_x, max_y)
        LR = (max_x, min_y)

        #step3: now lets get the area for global points and also for the local points 
        global_area = (max_x - min_x)*(max_y-min_y)
        total_local_area = 0 
        for point in rectangles:
            total_local_area += (point[2] - point[0])*(point[3]-point[1])
        if total_local_area != global_area:
            #print("AREA MISMATCH")
            return False 
        
        #step4: now lets count all_points and check the overlap condition
        my_dict = {}
        for point in all_points:
            if (point[0],point[1]) not in my_dict:
                my_dict[(point[0],point[1])] = 1 
            else:
                my_dict[(point[0],point[1])] += 1 
        
        if LL not in my_dict or UR not in my_dict or UL not in my_dict or LR not in my_dict:
            #print("corner not in dict")
            return False  
        
        check_dict = {LL, UR, UL, LR}
        #print(my_dict)
        #print(check_dict)

        if my_dict[LL] != 1 or my_dict[UR] != 1 or my_dict[UL] != 1 or my_dict[LR] != 1: 
            return False 
        
        for key in my_dict:
            if my_dict[key] == 1 and key not in check_dict:
                #print("HERE1")
                return False 
            
            elif my_dict[key] ==1 and key in check_dict:
                continue 

            elif my_dict[key] not in {1,2,4}: 
                #print("HERE2")
                return False 
            
        return True 

test = Solution()
rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
print(test.isRectangleCover(rectangles))