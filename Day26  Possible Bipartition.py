class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # Constant defined for color drawing to person
        NOT_COLORED, BLUE, GREEN = 0, 1, -1
        
        # -------------------------------------
        
        def helper( person_id, color ):
            
            # Draw person_id as color
            color_table[person_id] = color
            
            # Draw the_other, with opposite color, in dislike table of current person_id
            for the_other in dislike_table[ person_id ]:
   
                if color_table[the_other] == color:
                    # the_other has the same color of current person_id
                    # Reject due to breaking the relationship of dislike
                    return False

                if color_table[the_other] == NOT_COLORED and (not helper( the_other, -color)):
                    # other people can not be colored and keeping dis-like relationship
                    return False
                    
            return True
        
        
        # ------------------------------------------------
        if N == 1 or not dislikes:
            # Quick response for simple cases
            return True
        
        
        
        # each person maintain a list of dislike
        dislike_table = collections.defaultdict( list )
        
        # cell_#0 is dummy just for the convenience of indexing from 1 to N
        color_table = [ NOT_COLORED for _ in range(N+1) ]
        
        for p1, p2 in dislikes:
            
            # P1 and P2 dislike each other
            dislike_table[p1].append( p2 )
            dislike_table[p2].append( p1 )
            
        
        # Try to draw dislike pair with different colors in DFS
        for person_id in range(1, N+1):
            
            if color_table[person_id] == NOT_COLORED and (not helper( person_id, BLUE)):
                
                return False 
        
        return True
    