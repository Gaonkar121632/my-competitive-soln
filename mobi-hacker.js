const reducer = (accumulator, currentValue) => Number(accumulator) + Number(currentValue);
let prevCount=Infinity,currentCount=0,count=0;
function findValue(params) {
    for (let index = params; params > 0; index--) {   
        let numberArra=index.toString().split('');
        let number =numberArra.reduce(reducer)
        currentCount=number;
        if (Number(currentCount)< prevCount) {
            prevCount=currentCount;
            count++;
        }
        else if(Number(currentCount)>prevCount){
        return count
        }
    }
}

let x=findValue(31);
console.log(x);
