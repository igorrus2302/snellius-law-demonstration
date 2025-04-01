import numpy as np
import matplotlib.pyplot as plt


# Функция для вычисления угла преломления по закону Снеллиуса
def snell_law(n1, n2, theta1):
    if n1 > n2:  # Проверка на полное внутреннее отражение
        critical_angle = np.degrees(np.arcsin(n2 / n1))
        if theta1 > critical_angle:
            return None  # Полное внутреннее отражение
    return np.degrees(np.arcsin(n1 * np.sin(np.radians(theta1)) / n2))


# Функция для построения хода луча
def draw_light_path(n_values, theta_incident):
    fig, ax = plt.subplots(figsize=(8, len(n_values) * 1.5))
    y = 5  # Начальная координата по Y (чтобы падал сверху)
    x = 0  # Начальная координата по X (по центру)
    dx = 6  # Горизонтальный шаг для визуализации
    theta = theta_incident  # Текущий угол падения

    # Рисуем слои сред
    for i in range(len(n_values)):
        ax.axhline(-i * 3, color='k', linewidth=1)

    # Начальные координаты
    x_prev, y_prev = x, y
    x_next = x + dx * np.tan(np.radians(theta))
    y_next = 0

    # Рисуем падающий луч
    ax.plot([x_prev, x_next], [y_prev, y_next], 'r-', linewidth=2)
    ax.text((x_prev + x_next) / 2, (y_prev + y_next) / 2, f'{theta:.1f}°', color='b', fontsize=10)
    x_prev, y_prev = x_next, y_next

    # Рисуем дальнейший путь луча через среды
    for i in range(len(n_values) - 1):
        n1, n2 = n_values[i], n_values[i + 1]
        theta_next = snell_law(n1, n2, theta)

        # Рисуем перпендикуляр
        ax.plot([x_prev, x_prev], [y_prev - 1, y_prev + 1], 'g--', linewidth=1)

        if theta_next is None:  # Полное внутреннее отражение
            theta = 180 - theta  # Отражение
        else:
            theta = theta_next  # Преломленный угол

        x_next = x_prev + dx * np.tan(np.radians(theta))
        y_next = - (i + 1) * 3  # Следующий уровень слоя
        ax.plot([x_prev, x_next], [y_prev, y_next], 'r-', linewidth=2)
        ax.text((x_prev + x_next) / 2, (y_prev + y_next) / 2, f'{theta:.1f}°', color='b', fontsize=10)
        x_prev, y_prev = x_next, y_next

    ax.set_xlim(-10, 10)
    ax.set_ylim(-len(n_values) * 3, 6)
    ax.set_xlabel("X")
    ax.set_ylabel("Medium Layers")
    ax.set_title("Light Refraction through Different Media")
    plt.gca().invert_yaxis()
    plt.show()


# Ввод данных
num_layers = int(input("Введите количество сред: "))
n_values = [float(input(f"Введите показатель преломления для среды {i + 1}: ")) for i in range(num_layers)]
theta_incident = float(input("Введите угол падения луча (в градусах): "))

draw_light_path(n_values, theta_incident)
