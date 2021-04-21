function writeToDocument(message) {
    document.writeln(message);
}

function printWithValue(name, value) {
    document.writeln(name + " -> " + value);
}

function sayHello(value) {
    let v = value < 30 ? document.writeln("Hello World!") : document.writeln("Hello Javascript!");
    return v;
}

function getAverage(a, b) {
    let avg = (a + b) / 2;
    return avg;
}

function isEven(number) {
    let n = number % 2 == 0 ? (number == 0 ? document.writeln("This is zero") : document.writeln(number + " is even")) : document.writeln(number + " is odd");
    return n;
}
// 배열의 원소를 반환하는 함수를 정의
let item = ["Apple", "Banana", "Candy", "Doll"];
function getItem(n){
    if ( n < 0 || n >= item.length) { 
        //return키워드는 함수내에서 반드시 하나일 필요는 없다.
        
        return "No item";
    }
    return item[n];
}


