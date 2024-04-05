const input = document.querySelector('#input');
const main = document.querySelector('main');
const output = document.querySelector('#output');
const keyOutput = document.querySelector('#key');

input.addEventListener('input', function() {
    const value = input.value;
    if (value === '') {
        main.classList.remove('valid');
        return;
    } else {
        main.classList.add('valid');
        encrypted = encrypt(value);
        output.textContent = encrypted[0];
        keyOutput.textContent = encrypted[1];
    }
});

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function toBinaryMatrix(str) {
    return [...str].map(char => char.charCodeAt(0).toString(2).padStart(8, '0').split('').map(Number));
}

function fromBinaryMatrix(matrix) {
    return matrix.map(row => String.fromCharCode(parseInt(row.join(''), 2))).join('');
}

function xorMatrices(matrix1, matrix2) {
    return matrix1.map((row, i) => row.map((bit, j) => bit ^ matrix2[i][j]));
}

// Encrypt
function encrypt(input) {
    try {
        const key = Array.from({length: input.length}, () => String.fromCharCode(getRandomInt(33, 126))).join('');
        const matrix = toBinaryMatrix(input);
        const keyMatrix = toBinaryMatrix(key);
        const output = fromBinaryMatrix(xorMatrices(matrix, keyMatrix));
        return [output, key];
    } catch (e) {
        return false;
    }
}

// Decrypt
function decrypt(input, key) {
    try {
        const matrix = toBinaryMatrix(input);
        const keyMatrix = toBinaryMatrix(key);
        const output = fromBinaryMatrix(xorMatrices(matrix, keyMatrix));
        return output;
    } catch (e) {
        return false;
    }
}