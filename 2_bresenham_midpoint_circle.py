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

def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r

    draw_circle(xc, yc, x, y)

    while y >= x:
        x += 1

        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

        draw_circle(xc, yc, x, y)

# Çemberin merkezi ve yarı çapını belirleyin
xc, yc = 5, 5
radius = 4

# Bresenham çember algoritmasını kullanarak çizimi yapın
bresenham_circle(xc, yc, radius)

# Sonucu görselleştirin
plt.title('Bresenham Orta Nokta Çember Algoritması Örneği')
plt.xlabel('X Eksen')
plt.ylabel('Y Eksen')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
