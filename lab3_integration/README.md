## Лабораторная работа №3. Численное интегрирование

**Цель работы:** найти приближенное значение определенного интеграла с требуемой точностью различными численными методами.

### Вариант 17
- Метод прямоугольников (все)
- Метод трапеций

`integral (-x^3 - x^2 - 2x + 1)dx from 0 to 2`

### Обязательное задание

1. Пользователь выбирает функцию, интеграл которой требуется вычислить (3-5 функций), из тех, которые предлагает программа.
2. Пределы интегрирования задаются пользователем.
3. Точность вычисления задается пользователем.
4. Начальное значение числа разбиения интервала интегрирования: `n=4`.
5. Ввод исходных данных осуществляется с клавиатуры.

#### Программная реализация задачи

1. Реализовать в программе методы по выбору пользователя, исходя из варианта:
   - Метод прямоугольников (3 модификации: левые, правые, средние)
   - Метод трапеций
   - Метод Симпсона
2. Методы должны быть оформлены в виде отдельной(ого) функции/класса.
3. Вычисление значений функции оформить в виде отдельной(ого) функции/класса.
4. Для оценки погрешности и завершения вычислительного процесса использовать правило Рунге.
5. Предусмотреть вывод результатов: значение интеграла, число разбиения интервала интегрирования для достижения требуемой точности.

#### Вычислительная реализация задачи

1. Вычислить интеграл, приведенный в таблице 1 (столбец 3), точно.
        -8.66666666667
2. Вычислить интеграл по формуле Ньютона – Котеса при `n=6`.
        с0 = с6 = 
3. Вычислить интеграл по формулам средних прямоугольников, трапеций и Симпсона при  `n=6`.
4. Сравнить результаты с точным значением интеграла.
5. Определить относительную погрешность вычислений.
6. В отчете отразить последовательные вычисления.

### Необязательное задание

1. Установить сходимость рассматриваемых несобственных интегралов  2 рода (2-3 функции). Если интеграл - расходящийся, выводить сообщение: «Интеграл не существует».
2. Если интеграл сходящийся, реализовать в программе вычисление несобственных интегралов 2 рода (заданными численными методами). 
3. Рассмотреть случаи, когда подынтегральная  функция терпит бесконечный разрыв: 1) в точке a, 2) в точке b, 3) на отрезке интегрирования 

### Оформить отчет, который должен содержать:
1. Титульный лист.
2. Цель лабораторной работы.
3. Порядок выполнения работы.
4. Рабочие формулы методов.
5. Листинг программы.
6. Результаты выполнения программы.
7. Вычисление заданного интеграла.
8. Выводы
