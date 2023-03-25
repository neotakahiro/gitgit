import matplotlib.pyplot as plt

# 物質の性質
thickness = 0.1    # 厚さ (m)
area = 1.0         # 断熱面積 (m^2)
q_list = [10, 20, 30, 40, 50]   # 熱流束のリスト (W/m^2)

# 熱伝導率の計算
k_list = []
for q in q_list:
    k = q * thickness / area
    k_list.append(k)

# 結果の表示
print("熱流束 (W/m^2):", q_list)
print("熱伝導率 (W/m/K):", k_list)

# 結果の図示
plt.plot(q_list, k_list)
plt.title("Thermal Conductivity")
plt.xlabel("Heat Flux (W/m^2)")
plt.ylabel("Thermal Conductivity (W/m/K)")
plt.show()
