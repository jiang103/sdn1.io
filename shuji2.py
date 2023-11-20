import random

class CountMinSketch:
    def __init__(self, w, d):
        self.w = w
        self.d = d
        self.table = [[0] * w for _ in range(d)]

    def add(self, item):
        for i in range(self.d):
            index = hash(item + str(i)) % self.w
            self.table[i][index] += 1

    def estimate(self, item):
        min_count = float('inf')
        for i in range(self.d):
            index = hash(item + str(i)) % self.w
            min_count = min(min_count, self.table[i][index])
        return min_count
# 假设数据集已经按照五元组进行了标记
flows = [("192.168.1.1", "192.168.1.2", 80, 80, "TCP"),
         ("192.168.1.1", "192.168.1.2", 80, 80, "TCP"),
         ("192.168.1.1", "192.168.1.2", 443, 443, "TCP"),
         ("192.168.1.1", "192.168.1.2", 80, 80, "UDP"),
         ("192.168.1.1", "192.168.1.2", 80, 80, "TCP")]

# 初始化 Count-Min Sketch
cms = CountMinSketch(100, 5)

# 添加数据流到 Count-Min Sketch
for flow in flows:
    cms.add(flow)

# 估计每个流的出现次数
estimated_counts = {flow: cms.estimate(flow) for flow in set(flows)}
print(estimated_counts)
# 计算精确值
exact_counts = {flow: flows.count(flow) for flow in set(flows)}

# 计算评估指标
precision = sum([min(estimated_counts[flow], exact_counts[flow]) / estimated_counts[flow] for flow in estimated_counts]) / len(estimated_counts)
accuracy = sum([min(estimated_counts[flow], exact_counts[flow]) for flow in estimated_counts]) / sum(exact_counts.values())
recall = sum([min(estimated_counts[flow], exact_counts[flow]) for flow in estimated_counts]) / sum(exact_counts.values())
f1_score = 2 * precision * recall / (precision + recall)

print("Precision:", precision)
print("Accuracy:", accuracy)
print("Recall:", recall)
print("F1-Score:", f1_score)
