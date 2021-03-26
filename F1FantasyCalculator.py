# This calculates the optimal team using data from the LAST season of f1
class Team():
    def __init__(self, drivers, constructors):
        self.Drivers = drivers
        self.Constructors = constructors
        self.Budget = 100
        self.noDrivers = 5
        self.Rankings = self.sortTeamsByPoints()

    def getPossibleTeams(self):
        """
        # Iterates through every possible combination, eliminating over budget teams and sorting by points total
        viableTeams = []
        DriverNames = list(self.Drivers.keys())
        ConstructorNames = list(self.Constructors.keys())
        #cheapestConstructorPrice = ConstructorsData[ConstructorNames[-1]]["Price"]
        for DriverCombo in CombinationCalc(DriverNames, 5).GetResult():
            total = self.Budget
            teamPoints = 0

            for driver in DriverCombo:
                total -= self.Drivers[driver]["Price"]
                teamPoints += self.Drivers[driver]["Points"]
            #if total < cheapestConstructorPrice:
            if total < 0:
                pass # that combo is thrown out
            else:
                for constructor in ConstructorNames:
                    total -= self.Constructors[constructor]["Price"]
                    if total < 0:
                        pass
                    else:
                        teamPoints += self.Constructors[constructor]["Points"]
                        viableTeams.append({"Drivers" : DriverCombo, "Constructor" : constructor, "Points" : teamPoints})"""
        viableTeams = []
        DriverNames = list(self.Drivers.keys())
        ConstructorNames = list(self.Constructors.keys())
        for combo in CombinationCalc(DriverNames, 5).GetResult():
            cost = 0
            points = 0
            for driver in combo:
                cost += self.Drivers[driver]["Price"]
                points += self.Drivers[driver]["Points"]
            for constructor in ConstructorNames:
                cost += self.Constructors[constructor]["Price"]
                points += self.Constructors[constructor]["Points"]
                viableTeams.append({"Drivers" : combo, "Constructor" : constructor, "Points" : points, "Cost" : cost})

        print(len(viableTeams))

        return viableTeams

    def sortTeamsByPoints(self):
        teamsToSort = self.getPossibleTeams()
        MergeSort().Sort(teamsToSort)
        return  teamsToSort


class MergeSort:

    def Sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.Sort(left)
            self.Sort(right)
            i,j, k = 0,0,0

            while i < len(left) and j < len(right):

                # FLIP THE OPERATOR TO REVERSE THE ORDER
                if left[i]["Points"] >right[j]["Points"]:
                    arr[k] = left[i]
                    i+= 1

                else:
                    arr[k] = right[j]
                    j+=1
                k+=1


            while i < len(left):
                arr[k] = left[i]
                i+=1
                k+=1

            while j < len(right):
                arr[k] = right[j]
                j+=1
                k+=1




class CombinationCalc:
    """
    Use CombinationCalc([array], numberofcombos).GetResult() to get the array of combinations
    """
    def __init__(self, arr, r):
        self.result = []
        self.getCombination(arr, r)
        self.GetResult()


    def GetResult(self):
        return self.result

    # For array to generate combos of size r
    def getCombination(self, arr, r):
        n = len(arr)
        data = [0] * r
        self._combineUntil(arr, data, 0, n - 1, 0, r)

    def _combineUntil(self, arr, data, startIndex, endIndex, currentIndex, r):
        if currentIndex == r:
            combo = []
            for j in range(r):
                combo.append(data[j])
            self.result.append(combo)
            return

        i = startIndex
        while (i <= endIndex) and (endIndex - i + 1 >= r - currentIndex):
            data[currentIndex] = arr[i]
            self._combineUntil(arr, data, i + 1, endIndex, currentIndex + 1, r)
            i += 1






DriversData ={
 "Hamilton": {"Price": 33.5  ,  "Points": 40.82},
 "Verstappen": {"Price": 24.8 ,   "Points": 26.88},
 "Bottas": {"Price": 23.6   , "Points": 25.59},
 "Perez": {"Price": 18.4   , "Points": 18.71},
 "Ricciardo": {"Price": 17.3,    "Points": 21.41},
 "Leclerc": {"Price": 16.8   , "Points": 14},
 "Vettel": {"Price": 16.2    ,"Points": 10},
 "Alonso": {"Price": 15.6    ,"Points": 13},
 "Sainz": {"Price": 14.4    ,"Points": 15.88},
 "Stroll": {"Price": 13.9    ,"Points": 10.53},
 "Norris": {"Price": 13.1    ,"Points": 17.71},
 "Gasly": {"Price": 11.7    ,"Points": 11.3},
 "Ocon": {"Price": 10.1    ,"Points": 8.76},
 "Raikkonen": {"Price": 9.6 ,   "Points": 10.53},
 "Tsunoda": {"Price": 8.8    ,"Points": 9},
 "Giovinazzi": {"Price": 7.9  ,  "Points": 6.06},
 "Latifi": {"Price": 6.5   , "Points": 4.71},
 "Russell": {"Price": 6.2   , "Points": 4.53},
 "Schumacher": {"Price": 5.8 ,   "Points": 4},
 "Mazepin": {"Price": 5.5   , "Points": 4}}

ConstructorsData ={
 "Mercedes": {"Price": 38.0    ,"Points": 59.6},
 "Red Bull": {"Price": 25.9    ,"Points": 48},
 "McLaren": {"Price": 18.9   , "Points": 30.4},
 "Ferrari": {"Price": 18.1    ,"Points": 21.5},
 "Aston Martin": {"Price": 17.6,    "Points": 28.9},
 "Alpine": {"Price": 15.4    ,"Points": 28.1},
 "Alpha Tauri": {"Price": 12.7 ,   "Points": 20.9},
 "Alfa Romeo": {"Price": 8.9   , "Points": 15.1},
 "Williams": {"Price": 6.3    ,"Points": 10.4},
 "Haas": {"Price": 6.1    ,"Points": 9.6}, }

print(Team(DriversData, ConstructorsData).getPossibleTeams()[0:10])
input()
