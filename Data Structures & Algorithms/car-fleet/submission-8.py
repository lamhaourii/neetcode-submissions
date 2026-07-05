class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos=[(posi,i) for i,posi in enumerate(position)]
        sorted_position=sorted(pos, reverse=True)
        sorted_pos=[position[po[1]] for po in sorted_position]
        sorted_spd=[speed[po[1]] for po in sorted_position]
        time= [(target-sorted_pos[i])/sorted_spd[i] for i in range(len(sorted_spd))]
        fleet=[]
        for i in range(len(sorted_pos)):
            
            if fleet and time[i]<=fleet[-1]:
                continue
            else: 
                fleet.append(time[i])
        return len(fleet)


        

            


        