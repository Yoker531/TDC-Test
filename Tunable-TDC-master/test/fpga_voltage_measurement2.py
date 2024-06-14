import burn
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# 配置FPGA设计
design = burn.z1.picorv.picorv32.baseOverlay("picorv32.bit")

# 假设的电压测量函数
def measure_voltage():
    # 这里放置从硬件设备获取电压的实际代码
    # 例如，调用硬件接口库的函数读取电压数据
    return np.random.uniform(0, 5)  # 真实情况应替换为实际测量值

# 执行背景扫描
def perform_background_scan():
    base_sweep = [measure_voltage() for _ in range(100)]
    plt.plot(base_sweep)
    plt.xlabel("Phi Offset")
    plt.ylabel("Popcount")
    plt.title("Base Sweep")
    plt.savefig('outputs/base_sweep.png')
    plt.show()
    return base_sweep

# AES加密和解密函数
def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    return encrypted_data

def decrypt_data(encrypted_data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return decrypted_data

# 示例密钥（16字节）
key = b'Sixteen byte key'

# 设置AES计算参数
def load_aes_task():
    args = np.array([], np.int32)
    design.processor.load(aes, args)  # 加载但不启动AES

# 启动AES计算
def start_aes_task():
    design.processor.start(aes)  # 启动AES

# 执行动态扫描
def perform_dynamic_scan():
    dynamic_sweep = [measure_voltage() for _ in range(100)]
    plt.plot(dynamic_sweep)
    plt.xlabel("Phi Offset")
    plt.ylabel("Popcount")
    plt.title("Dynamic Sweep with AES Running")
    plt.savefig('outputs/dynamic_sweep.png')
    plt.show()
    return dynamic_sweep

# 测量电压并加密数据
def measure_and_encrypt_voltage():
    voltage = measure_voltage()  # 真实的电压测量
    voltage_str = f"{voltage:.2f}V"
    print(f"Measured voltage: {voltage_str}")
    
    # 加密电压数据
    encrypted_voltage = encrypt_data(voltage_str.encode(), key)
    print(f"Encrypted voltage data: {encrypted_voltage}")
    
    # 解密电压数据
    decrypted_voltage = decrypt_data(encrypted_voltage, key).decode()
    print(f"Decrypted voltage data: {decrypted_voltage}")

# 执行扫描并测量加密电压
base_sweep = perform_background_scan()  # 获取背景扫描
load_aes_task()  # 加载AES任务到核心
start_aes_task()  # 启动AES任务
dynamic_sweep = perform_dynamic_scan()  # 获取动态扫描
measure_and_encrypt_voltage()  # 测量并加密电压数据
