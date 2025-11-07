import numpy as np
import matplotlib
# Якщо запускаєш на сервері/CI без дисплея, використовуємо бекстенд "Agg" для збереження файлів
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# Діапазон значень x
x = np.linspace(1, 10, 500)

# Обчислення значень функції
y = 5 * np.sin(x) * (np.cos(x**2 + 1/x))**2

# Побудова графіка
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, linestyle='-', linewidth=2, color='blue',
        label=r'$Y(x)=5\sin(x)\cos^2\!\left(x^2+\frac{1}{x}\right)$')

ax.set_xlabel('x')
ax.set_ylabel('Y(x)')
ax.set_title('Графік функції Y(x) = 5*sin(x) * cos(x^2 + 1/x)^2')
ax.legend()
ax.grid(True)

# Зберігаємо файл у робочій директорії
out_fname = 'plot.png'
plt.tight_layout()
plt.savefig(out_fname, dpi=300, bbox_inches='tight')

print(f'Графік збережено у файл: {os.path.abspath(out_fname)}')
