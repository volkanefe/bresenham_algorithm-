import matplotlib.pyplot as plt

def draw_circle(xc, yc, x, y):
    plt.scatter(xc + x, yc + y, color='blue')  # 1. bölge
    plt.scatter(xc - x, yc + y, color='blue')  # 2. bölge
    plt.scatter(xc + x, yc - y, color='blue')  # 3. bölge
    plt.scatter(xc - x, yc - y, color='blue')  # 4. bölge
    plt.scatter(xc + y, yc + x, color='blue')  # 5. bölge
    plt.scatter(xc - y, yc + x, color='blue')  # 6. bölge
    plt.scatter(xc + y, yc - x, color='blue')  # 7. bölge
    plt.scatter(xc - y, yc - x, color='blue')  # 8. bölge

def mid_point_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    draw_circle(xc, yc, x, y)

    while x < y:
        x += 1

        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1

        draw_circle(xc, yc, x, y)

# Dairenin merkezi ve yarıçapını belirleyin
xc, yc = 5, 5
radius = 4

# Orta nokta daire çizim algoritmasını kullanarak çizimi yapın
mid_point_circle(xc, yc, radius)

# Sonucu görselleştirin
plt.title('Orta Nokta Daire Çizim Algoritması Örneği')
plt.xlabel('X Eksen')
plt.ylabel('Y Eksen')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
