let ROW = 50;
let COL = 50;
let twoD = Array(ROW).fill().map(() => Array(COL).fill(1));
function isValid(row, col) {
    // return true if row number and column number 
    // is in range 
    return (row >= 0) && (row < ROW) &&
        (col >= 0) && (col < COL);
}
let rowNum = [-1, 0, 0, 1];
let colNum = [0, -1, 1, 0];
let findDestination = (matrix,src, dest) => {
  return new Promise((resolve,reject)=>{
  console.log(src,dest)
    // let matrix = Array(ROW).fill().map(() => Array(COL).fill(1));
    let visited = Array(ROW).fill().map(() => Array(COL).fill(0));
    visited[src.x][src.y] = true;
    q = [];
    s = { pt: src, dist: [[src.x, src.y]] };
    q.push(s);

    while (q.length > 0) {


        let curr = q.shift()
        let pt = curr.pt
        if (pt.x == dest.x && pt.y == dest.y) {
             resolve(curr.dist);
            // return curr.dist
        }
        // q.pop()

        for (let i = 0; i < 4; i++) {
            let x = pt.x + rowNum[i];
            let y = pt.y + colNum[i];

            // if adjacent cell is valid, has path and 
            // not visited yet, enqueue it. 
            if (isValid(x, y) && matrix[x][y] &&
                !visited[x][y]) {

                // mark cell as visited and enqueue it 
                visited[x][y] = true;
                let tempArr = curr.dist.concat([[x, y]])
                let Adjcell = { pt: { x, y }, dist: tempArr };
                q.unshift(Adjcell);
            }
        }
    }
    resolve(-1)
    // return -1
  })
  }

findDestination(twoD, { x: 1, y: 1 }, { x: 5, y: 7 }).then(res=>{
console.log(res);
})