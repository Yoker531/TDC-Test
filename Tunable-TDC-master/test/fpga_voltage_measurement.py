import burn 
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# 配置FPGA设计
design = burn.z1.picorv.picorv32.baseOverlay("picorv32.bit")

# 执行背景扫描
base_sweep = np.random.rand(100)  # 模拟数据，替换为实际扫描代码
plt.plot(base_sweep)
plt.xlabel("Phi Offset")
plt.ylabel("Popcount")
plt.title("Base Sweep")
plt.savefig('outputs/base_sweep.png')
plt.show()

# 设置AES计算参数并启动
args = np.array([], np.int32)
design.processor.launch(aes, args)

# 执行动态扫描
dynamic_sweep = np.random.rand(100)  # 模拟数据，替换为实际扫描代码
plt.plot(dynamic_sweep)
plt.xlabel("Phi Offset")
plt.ylabel("Popcount")
plt.title("Dynamic Sweep with AES Running")
plt.savefig('outputs/dynamic_sweep.png')
plt.show()
