import numpy as np


class GradeStatistics:
  def __init__(self, x):
    self.x = x
    
  def mean(self):
        return np.mean(self.x)
    
  def median(self):
        return np.median(self.x)
    
  def mode(self):
        return round(max(set(list(self.x)),key=list(self.x).count))
    
  def variance(self):
       return (np.var(self.x))
   
  def standard_deviation(self):
     return (np.std(self.x))
 

arr=np.array([1,2,3,4,5,2,5,6])


fin = GradeStatistics(arr)


print("The mean is:",fin.mean())
print("The median is:",fin.median())
print("The mode is:",fin.mode())
print("The variance is:",fin.variance())
print("The standard deviation is:",fin.standard_deviation())


#Mean is very important because it gives an approximate idea of how the numbers in the data set turns out.
#Medain is very important cause it helps find the middle value of a data set after putiing it in order.
#Mode is important cause it lets us know the number that is the most frequent in the data set.
#variance is very important to investors cause it can typically show how much of a risk somthing is.
#Standard deviation is really important because it shows how spread out the data points are in the data set.