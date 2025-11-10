// Фон с плавающими анимированными кругами
class FloatingCirclesBackground {
    constructor(elementId) {
        this.background = document.getElementById(elementId);
        this.circles = [];
        this.init();
    }

    init() {
        this.createCircles();
        this.animateCircles();

        // Пересоздаем круги при изменении размера окна
        window.addEventListener('resize', () => {
            this.circles.forEach(circle => circle.remove());
            this.createCircles();
        });
    }

    createCircles() {
        const circleCount = 25;

        for (let i = 0; i < circleCount; i++) {
            const circle = document.createElement('div');
            circle.className = 'floating-circle';

            // Случайные параметры
            const size = Math.random() * 100 + 50;
            const posX = Math.random() * 100;
            const posY = Math.random() * 100;
            const opacity = Math.random() * 0.3 + 0.1;
            const color = this.getRandomColor();

            circle.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                background: ${color};
                border-radius: 50%;
                opacity: ${opacity};
                left: ${posX}%;
                top: ${posY}%;
                filter: blur(${Math.random() * 20 + 5}px);
                transform: translate(-50%, -50%);
            `;

            this.background.appendChild(circle);
            this.circles.push({
                element: circle,
                x: posX,
                y: posY,
                speedX: (Math.random() - 0.5) * 0.3,
                speedY: (Math.random() - 0.5) * 0.3,
                size: size
            });
        }
    }

    animateCircles() {
        this.circles.forEach(circle => {
            // Обновляем позицию
            circle.x += circle.speedX;
            circle.y += circle.speedY;

            // Отскакиваем от границ
            if (circle.x > 100 || circle.x < 0) circle.speedX *= -1;
            if (circle.y > 100 || circle.y < 0) circle.speedY *= -1;

            // Применяем новую позицию
            circle.element.style.left = circle.x + '%';
            circle.element.style.top = circle.y + '%';
        });

        requestAnimationFrame(() => this.animateCircles());
    }

    getRandomColor() {
        const colors = [
            'rgba(102, 126, 234, 0.6)',   // Фиолетовый
            'rgba(240, 147, 251, 0.6)',   // Розовый
            'rgba(79, 172, 254, 0.6)',    // Синий
            'rgba(67, 233, 123, 0.6)',    // Зеленый
            'rgba(250, 112, 154, 0.6)'    // Оранжевый
        ];
        return colors[Math.floor(Math.random() * colors.length)];
    }
}

// Инициализация
document.addEventListener('DOMContentLoaded', function() {
    new FloatingCirclesBackground('animatedBackground');
});