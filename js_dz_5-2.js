
function Item(product, image, price, quantity, discount = 0) {
    this.product = product;
    this.image = `../img/${image}.png`;
    this.price = price;
    this.quantity = quantity;
    this.discount = discount;
    this.finalPrice = function () {
        if (this.discount != 0) {
            return this.price - this.price * this.discount / 100;
        } else {
            return this.price;
        }
    }
    this.showMyChart = function () {
        return `${this.product} (Количество: ${this.quantity})`;
    }
}

let bascket = []

bascket.push(
    new Item('product_1', 'imge_1', 100, 5)
);
bascket.push(
    new Item('product_2', 'imge_2', 117, 2, 7)
);
bascket.push(
    new Item('product_3', 'imge_3', 115, 3)
);
bascket.push(
    new Item('product_4', 'imge_4', 50, 4)
);
bascket.push(
    new Item('product_5', 'imge_5', 90, 1, 12)
);

// console.log(bascket)

function finalChart(bascket
) {
    console.log('Ваш заказ: ')
    bascket
        .forEach(val => {
            console.log(`${val.showMyChart()}.
    Цена с учетом скидки: ${val.finalPrice()}.
    Стоимость: ${val.quantity * val.finalPrice()}`);
        });
}
finalChart(bascket
);


function finalCost(bascket
) {
    return bascket
        .reduce(function (acc, bascket
        ) {
            return acc + (bascket
                .finalPrice() * bascket
                    .quantity)
        }, 0)
};
console.log(('Итоговая стоимость: ' + finalCost(bascket
)).toUpperCase());