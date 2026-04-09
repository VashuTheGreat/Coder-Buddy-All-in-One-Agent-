let currentNumber = '';
let previousNumber = '';
let currentOperator = null;

document.querySelectorAll('.btn').forEach(button => {
  button.addEventListener('click', () => {
    const value = button.textContent;
    if (isNaN(value) && value !== '.') {
      handleOperator(value);
    } else {
      handleNumber(value);
    }
  });
});

function handleNumber(value) {
  if (value === '.' && currentNumber.includes('.')) return;
  currentNumber += value;
  updateDisplay();
}

function handleOperator(operator) {
  if (currentNumber === '') return;
  if (previousNumber !== '') {
    calculate();
  }
  previousNumber = currentNumber;
  currentNumber = '';
  currentOperator = operator;
}

function calculate() {
  let result;
  const prev = parseFloat(previousNumber);
  const current = parseFloat(currentNumber);
  if (isNaN(prev) || isNaN(current)) return;
  switch (currentOperator) {
    case '+':
      result = prev + current;
      break;
    case '-':
      result = prev - current;
      break;
    case '*':
      result = prev * current;
      break;
    case '/':
      result = prev / current;
      break;
    default:
      return;
  }
  currentNumber = result.toString();
  previousNumber = '';
  currentOperator = null;
  updateDisplay();
}

function updateDisplay() {
  document.getElementById('display').textContent = currentNumber;
}

document.getElementById('clear').addEventListener('click', () => {
  currentNumber = '';
  previousNumber = '';
  currentOperator = null;
  updateDisplay();
});

document.getElementById('equals').addEventListener('click', () => {
  if (previousNumber === '' || currentNumber === '') return;
  calculate();
});