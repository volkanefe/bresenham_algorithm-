import matplotlib.pyplot as plt

def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while x0 != x1 or y0 != y1:
        points.append((x0, y0))
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    points.append((x0, y0))
    return points

# İki nokta belirleyin
x0, y0 = 1, 1
x1, y1 = 8, 5

# Bresenham çizgi algoritmasını kullanarak noktaları hesapla
line_points = bresenham_line(x0, y0, x1, y1)

# Sonuçları görselleştir
x, y = zip(*line_points)
plt.plot(x, y, marker='o')
plt.title('Bresenham Çizgi Algoritması Örneği')
plt.xlabel('X Eksen')
plt.ylabel('Y Eksen')
plt.grid(True)
plt.show()
