function findFactors(number) {
    const factors = [];

    for (let i = 1; i <= number; i++) {
        if (number % i === 0) {
            factors.push(i);
        }
    }

    return factors;
}

const number = 24;
const factors = findFactors(number);
console.log(`Factors of ${number} are: ${factors.join(', ')}`);
