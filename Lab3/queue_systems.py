
class InfiniteQueueWithCancelling:

    service_time = 0
    stream_intensity = 0
    service_intensity = 0
    absolute_bandwidth = 0

    def __init__(self, service_time, stream_intensity) -> None:
        self.service_time = service_time
        self.stream_intensity = stream_intensity
        self.service_intensity = 1/self.service_time
        self.absolute_bandwidth =  self.getFailureProbability() * self.service_intensity

    def getSuccessProbability(self):
        return self.service_intensity / (self.stream_intensity + self.service_intensity)

    def getFailureProbability(self):
        return self.stream_intensity / (self.stream_intensity + self.service_intensity)

    def getSuccessNumber(self,period_of_time):
        return self.absolute_bandwidth * period_of_time
    
    def getFailureNumber(self,period_of_time):
        return self.stream_intensity * self.getFailureProbability() * period_of_time
    
    def getStreamRatio(self,period_of_time):
        return self.getSuccessNumber(period_of_time)/self.getFailureNumber(period_of_time)

def printQueueSystemStats(service_time,stream_intensity):
    queue = InfiniteQueueWithCancelling(service_time,stream_intensity)
    print("Вероятность отказа")
    print(queue.getFailureProbability())
    print("Вероятность обслуживания")
    print(queue.getSuccessProbability())
    print("Отношение обслуженных заявок к необслуженным за 60 минут")
    print(queue.getStreamRatio(60))

print("Задача 1")
printQueueSystemStats(1,0.95)
print("_____________________")
print("Задача 3")
printQueueSystemStats(1,0.8)
print("_____________________")
print("Задача 5")
printQueueSystemStats(3,1)
print("_____________________")