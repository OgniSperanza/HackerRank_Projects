function processData(input) {
    var lines = input.split('\n');
    var dimension = parseInt(lines[0]);
    var grid = [];
    for(var i = 2; i <= dimension+1; ++i)
    {
        grid.push(lines[i]);
    }
    displayPathtoPrincess(dimension, grid);
}
function displayPathtoPrincess(dimension, grid)
{
   var mario = [];
   var princess = [];
   for (var i = 0; i < grid.length; i++){
       for (var j = 0; j < grid.length; j++){
           if (grid[i][j] == "m"){
                mario.push(i,j);
           }
           else if (grid[i][j] == "p"){
                princess.push(i,j);          
           }
       }
   }
   var moved = false;
   if (mario[0]<princess[0]){
       console.log("DOWN");
       moved = true;
   }
   else if (mario[0]>princess[0]){
       console.log("UP");
       moved = true;
   }
   if (moved!=true){
       if (mario[1]<princess[1]){
           console.log("RIGHT");
        }
        else if (mario[1]>princess[1]){
            console.log("LEFT");
        }
   }
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
