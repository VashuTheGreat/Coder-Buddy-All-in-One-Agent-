const buttons = document.querySelectorAll('.btn');
let currentExpression = '';
buttons.forEach(button => button.addEventListener('click', (e) => {
const display = document.getElementById('display');
let currentExpression = '';
if (e.target.value === '=') {
    try {
        display.value = eval(currentExpression);
    } catch (error) {
        display.value = 'Error';
    }
else if (e.target.value === 'C') {
    currentExpression = '';
    display.value = '';
} else {
    currentExpression += e.target.value;
    display.value = currentExpression;
}
        display.value = currentExpression;
    }
});
    }));

}
));