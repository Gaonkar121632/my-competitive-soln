// let x=`2
// 6
// 10 20 50 100 500 400 
// 30 20 60 70 90 490 
// 5
// 10 20 30 40 50 
// 40 50 60 70 80`

// let inputArray=x.split('\n')
// console.log(y);

// inputArray.forEach(element => {
//    console.log(element.match(/\s/));
// });

// for (let index = 0; index < inputArray.length; index++) {
//     let Flag="WIN"
//     if(inputArray[index].match(/\s/)){
//         let villan=inputArray[index].trim().split(' ');
//         let player=inputArray[index+1].trim().split(' ');
//         villan.sort((a,b)=>b-a)
//         player.sort((a,b)=>b-a)
        
//         for (let i = 0; i < villan.length; i++) {
//             if(Number(player[i])<=Number(villan[i])){
//                 Flag='LOSE'
//             }
//         }
//         console.log(Flag);  
//         index++;
//     }
// }

let inP=`5
5
-1 7 8 -5 4 
4
3 2 1 -1 
4
11 12 -2 -1 
4
4 5 4 3 
4
5 10 4 -1`
let inputArray=inP.split('\n');
let elmentArray=[]

for (let index = 0; index < inputArray.length; index++) {
        if(inputArray[index].match(/\s/)){
            let sample=inputArray[index].trim().split(' ').map(function(item) {
                return parseInt(item, 10);
            });
           let eleIndex= sample.indexOf(Math.max(...sample));
           let maxEle=sample.splice(eleIndex,1);
        
           caluculate(maxEle,eleIndex);
        }
}

function caluculate(num,indx){
    if(elmentArray.length==0){
        elmentArray.push({'num':num,'indx':indx})
    }else{


    }

}