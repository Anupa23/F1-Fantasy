class TeamGenerator:
    def __init__(self):
        pass
        self.budget = 100
        self.numberDrivers = 5
        self.driverCombos = []
        self.constructorNames = list(ConstructorsData.keys())
        # above statement takes precedence over other attributes here
        self.genDriverCombos()
        self.assignPriceNPoints()
        # Driver combos end with ... POINTS, PRICE], ... ]
        self.mergeSort(self.driverCombos)
        self.filterCombos()
        self.quickSort(self.driverCombos, 0, len(self.driverCombos) - 1)

    def genDriverCombos(self):
        driverNames = list(DriversData.keys())
        self._getCombinations(driverNames, len(driverNames), 5)

    def _getCombinations(self, arr, n, r):
        data = [0]*r
        self._combineUntil(arr, n, r, 0, data, 0)

    def _combineUntil(self, arr, n, r, index, data, i):
        if index == r:
            # add an extra indented loop encasing the following to add constructor
            for constructor in self.constructorNames:
                combo = []
                for j in range(r):
                    combo.append(data[j])
                combo.append(constructor)
                self.driverCombos.append(combo)
            return
        if i >= n:
            return
        data[index] = arr[i]
        self._combineUntil(arr, n, r, index+1, data, i+1)
        self._combineUntil(arr, n, r, index, data, i+1)

    def assignPriceNPoints(self):
        DriversData.update(ConstructorsData)
        for combo in self.driverCombos:
            totalPrice = sum([DriversData[itemName]["Price"] for itemName in combo])
            totalPoints = sum([DriversData[itemName]["Points"] for itemName in combo])
            combo.append(totalPoints)
            combo.append(totalPrice)

    def filterCombos(self):
        # find cut-off at cost just under budget (teams currently cost sorted highest to lowest)
        cutoff = self._binary_search(self.driverCombos, self.budget)
        self.driverCombos = self.driverCombos[cutoff:]



    def _binary_search(self, arr, x): # HYBRID BINARY AND LINEAR
        # works on sorted highest to lowest, switch operators otherwise
        low = 0
        high = len(arr) - 1
        mid = 0
        # all array will have [-1] at end because this is the cost
        result = 0

        while low <= high: # not this operator though

            mid = (high + low) // 2

            # If x is greater, ignore left half
            if arr[mid][-1] > x:
                low = mid + 1

            # If x is smaller, ignore right half
            elif arr[mid][-1] < x:
                high = mid - 1

            # means x is present at mid
            else:
                result = mid
                break

        # element not in data, so we return index of element directly
        # below searched element
        result = mid

        # NOW LINEAR SEARCH
        for i in range(result, -1, -1): #counts from where bin search left off towards start of list
            if arr[i][-1] > x:
                result = i + 1
                break

        return result

    def _partition(self, arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high][-2]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j][-2] >= pivot: # -2 for points
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)

    # mainquicksort function
    def quickSort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self._partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

    def mergeSort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]

            self.mergeSort(left)
            self.mergeSort(right)
            i, j, k = 0, 0, 0

            while i < len(left) and j < len(right):

                # FLIP THE OPERATOR TO REVERSE THE ORDER
                if left[i][-1] > right[j][-1]: # -1 because the prices are at end
                    arr[k] = left[i]
                    i += 1

                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1




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

Top10Teams = TeamGenerator().driverCombos[:10]
for team in Top10Teams:
    print(team)

input()

