from utils import *
import copy

class Kmeans():
    def __init__(self,k,data):
        self.data = data
        self.k = k
        self.tag = [-1 for i in range(len(self.data))]
        self.pri_tag = [-2 for i in range(len(self.data))]
        self.pri = []
        for i in range(self.k):
            self.pri.append(copy.deepcopy(self.data[i]))
        #self.pri.append(self.data[0])
        #self.pri.append(self.data[2])

    def gen_new(self):
        count = [0 for i in range(self.k)]
        add = [0 for i in range(self.k)]
        for i in range(len(self.data)):
            for j in range(self.k):
                if self.tag[i] == j:
                    count[j] = count[j]+1
                    if add[j] == 0:
                        add[j] = copy.deepcopy(self.data[i])
                    else:
                        for m in range(len(add[j])):
                            add[j][m] = add[j][m] + self.data[i][m]

        ans = []
        for i in range(len(count)):
            for j in range(len(add[i])):
                add[i][j] = add[i][j]/count[i]
            ans.append(add[i])
        return ans

    def is_same(self):
        for i in range(len(self.tag)):
            if self.tag[i]!=self.pri_tag[i]:
                return False
        return True

    def demo(self):
        for i in range(self.k):
            self.tag[i] = i

        while self.is_same() == False:
            self.pri_tag = copy.deepcopy(self.tag)
            for i in range(len(self.data)):
                min = 99999
                index = -1
                for j in range(self.k):
                    distance = cal_distance(self.pri[j],self.data[i])
                    if distance<min:
                        min = distance
                        index = j
                self.tag[i] = index

            self.pri = self.gen_new()
            print(self.tag)


        return self.tag




