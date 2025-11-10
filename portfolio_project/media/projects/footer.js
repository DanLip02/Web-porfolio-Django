class DynamicFooter {
    constructor() {
        this.footer = document.querySelector('footer');
        this.init();
    }

    init() {
        this.styleFooter();
        this.positionFooter();

        // Пересчитываем позицию при изменении размера окна
        window.addEventListener('resize', () => {
            this.positionFooter();
        });
    }

    styleFooter() {
        // Применяем темные стили
        this.footer.style.cssText = `
            background-color: #1a1a1a !important;
            color: #ffffff !important;
            text-align: center;
            padding: 20px 0;
            width: 100%;
            margin-top: auto;
            border-top: 2px solid #333;
        `;
    }

    positionFooter() {
        const body = document.body;
        const html = document.documentElement;

        // Высота всего документа
        const documentHeight = Math.max(
            body.scrollHeight,
            body.offsetHeight,
            html.clientHeight,
            html.scrollHeight,
            html.offsetHeight
        );

        // Высота видимой области
        const windowHeight = window.innerHeight;

        // Если контента мало - фиксируем футер внизу
        if (documentHeight <= windowHeight) {
            this.footer.style.position = 'fixed';
            this.footer.style.bottom = '0';
            this.footer.style.left = '0';
        } else {
            this.footer.style.position = 'relative';
            this.footer.style.bottom = 'auto';
        }
    }
}

// Инициализация когда страница загружена
document.addEventListener('DOMContentLoaded', function() {
    new DynamicFooter();
});

// Также обновляем когда контент изменяется (для динамического контента)
document.addEventListener('load', function() {
    new DynamicFooter();
});v