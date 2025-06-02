function calculator(num1, num2, operation) {
    switch(operation) {
        case 'add':
            return num1 + num2;
        case 'sub':
            return num1 - num2;
        case 'mul':
            return num1 * num2;
        case 'divide':
            if(num2 === 0) {
                return "Cannot divide by zero";
            }
            return num1 / num2;
        default:
            return "Invalid operation";
    }
}

// Example usage:
console.log(calculator(10, 5, 'add'));     
console.log(calculator(10, 5, 'sub'));     
console.log(calculator(10, 5, 'mul'));     
console.log(calculator(10, 5, 'divide'));  
console.log(calculator(10, 0, 'divide'));
