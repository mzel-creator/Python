// 1. С помощью цикла while вывести простые числа в промежутке от 0 до 100.

let i = 0;
while (i < 100) {
    if (isPrime(i)) {
        console.log(i);
    }
    i = i + 1;
}

function isPrime(num) {
    if (num < 2) {
        return false;
    }

    for (let i = 2; i < num; i++) {
        if (num % i === 0) {
            return false;
        }
    }

    return true;
}
// 2. Товары в корзине хранятся в массиве. Задачи:
// a) Организовать такой массив для хранения товаров в корзине;
// b) Организовать функцию countBasketPrice, которая будет считать стоимость корзины.

const basket = [
    ['Товар_1', 150],
    ['Товар_2', 170],
    ['Товар_3', 220],
];

const total = getTotalPrice(basket);

console.log(total);

function getTotalPrice(basket) {
    let result = 0;

    for (let item of basket) {
        result += item[1];
    }

    return result;
}

// 3. Вывести с помощью цикла for числа от 0 до 9, не используя тело цикла. Выглядеть это должно так: for (…) {// здесь пусто}

for (var number = 0; number <= 9;
    document.write(number++ + " ")) { }

// 4. Нарисовать пирамиду с помощью console.log, как показано на рисунке, только у вашей пирамиды должно быть 20 рядов, а не 5:

for (var i = 1, pyramid = " "; i <= 20; i++) {
    pyramid += "x";
    console.log(pyramid);
}