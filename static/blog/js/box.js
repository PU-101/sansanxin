var canvas=document.getElementById("box");
var ctx=canvas.getContext("2d");

var CANVAS_WIDTH = canvas.width;
var CANVAS_HEIGHT = canvas.height;
var STEP = CANVAS_WIDTH/8;

// 地图
// 0:空地，1:箱子，2:墙壁，3:目标地，4:箱子在目标地
var mapData = [
  [0,2,2,2,2,0,0,0],
  [0,2,0,0,2,2,0,0],
  [2,2,0,3,0,2,2,2],
  [2,0,0,0,0,3,0,2],
  [2,3,3,0,3,2,0,2],
  [2,0,0,0,0,0,0,2],
  [2,2,0,3,0,0,2,2],
  [0,2,2,2,2,2,2,0],
]

// 背景

var wallReady = false;
var wallImage = new Image();
wallImage.onload = function() {
  wallReady = true;
};
wallImage.src = "/static/blog/images/canvas/wall.png";
alert(wallImage.src)

var destinationReady = false;
var destinationImage = new Image();
destinationImage.onload = function() {
  destinationReady = true;
};
destinationImage.src = "/static/blog/images/canvas/destination.png";

var createMap = function() {
  // 背景色
  var grd = ctx.createLinearGradient(0, 0, 0, CANVAS_HEIGHT);
  grd.addColorStop(0, "#333");
  grd.addColorStop(1, "#999");
  ctx.fillStyle = grd;
  ctx.fillRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);

  var boxes = [];
  var box_index = 0;
  for (var r = 0; r < 8; r++) {
    for (var c = 0; c < 8; c++) {
      // 箱子
      // if (mapData[r][c] == 1) {
      //   if (boxReady) {
      //     boxes[box_index] = new Box({r: r, c: c});
      //     box_index += 1;
      //     ctx.drawImage(boxImage, 0,0,190,190, STEP*c, STEP*r, STEP, STEP);
      //   }
      // }
      // 墙壁
      if (mapData[r][c] == 2) {
        if (wallReady) {
          ctx.drawImage(wallImage, 0,0,161,161, STEP*c, STEP*r, STEP, STEP);
        }
      }
      // 目标地
      if (mapData[r][c] == 3) {
        if (destinationReady) {
          ctx.drawImage(destinationImage, 0,0,160,160, STEP*c, STEP*r, STEP, STEP);
        }
        
      }
    }
  }
}


// 人物
var personReady = false;
var personImage = new Image();
personImage.onload = function(){
  personReady = true;
}
personImage.src = '/static/blog/images/canvas/person.png';

var person = {
  speed: 50,
  direction: {x: 0, y: 0},
  positionMap: {r: 2, c: 2},
}

// 箱子
var boxReady = false;
var boxImage = new Image();
boxImage.onload = function(){
  boxReady = true;
}
boxImage.src = '/static/blog/images/canvas/box.png';

var boxReady = false;
var boxOkImage = new Image();
boxOkImage.onload = function() {
  boxOkReady = true;
}
boxOkImage.src = '/static/blog/images/canvas/box_ok.png';

var box = {
  positionMap: {r: 5, c: 5},
}

// class Box {
//   construct(positionMap) {
//     this.positionMap = positionMap;
//   } 
// }


// 转换为像素地址
var personPosition = {};
var boxPosition = {};
var convertToPosition = function(obj) {
  return {x: (obj.positionMap.c * STEP), y: (obj.positionMap.r * STEP)};
};

// 处理玩家输入
var key = {};
addEventListener('keyup', function(e) {
  key[e.keyCode] = true;
}, false);


// 重置
var reset = function() {
  person.positionMap.r = 2;
  person.positionMap.c = 2;
}

// 更新对象
var movePerson = function() {
  new_c = person.positionMap.c + person.direction.x;
  new_r = person.positionMap.r + person.direction.y;
  if (mapData[new_r][new_c] != 1 && mapData[new_r][new_c] != 2 && mapData[new_r][new_c] != 4) {
    person.positionMap.r = new_r;
    person.positionMap.c = new_c;
  }
};

var moveBox = function() {
  new_c = box.positionMap.c + person.direction.x;
  new_r = box.positionMap.r + person.direction.y;
  if ((box.positionMap.c - person.positionMap.c == person.direction.x) && (box.positionMap.r == person.positionMap.r)) {
    if (new_c > 0 && new_c < 15) {
      if (mapData[new_r][new_c] != 2) {
        if (mapData[box.positionMap.r][box.positionMap.c] == 4) {
          mapData[box.positionMap.r][box.positionMap.c] = 3;
        }
        else {
          mapData[box.positionMap.r][box.positionMap.c] = 0;
        }

        if (mapData[new_r][new_c] == 3) {
          mapData[new_r][new_c] = 4;
        }
        else {
          
          mapData[new_r][new_c] = 1;
        }

        box.positionMap.c = new_c;
      }
    }
  }

  if ((box.positionMap.r - person.positionMap.r == person.direction.y) && (box.positionMap.c == person.positionMap.c)) {
    if (new_r > 0 && new_r < 15) {
      if (mapData[new_r][new_c] != 2) {
        if (mapData[box.positionMap.r][box.positionMap.c] == 4) {
          mapData[box.positionMap.r][box.positionMap.c] = 3;
        }
        else {
          mapData[box.positionMap.r][box.positionMap.c] = 0;
        }

        if (mapData[new_r][new_c] == 3) {
          mapData[new_r][new_c] = 4; 
        }
        else {
          mapData[new_r][new_c] = 1;
        }

        box.positionMap.r = new_r;
      }
    }
  }
  
};

var move = function() {
  moveBox();
  movePerson();
}

var update = function(){

  if (person.positionMap.r > 0) {
    if (37 in key) {
      person.direction = {x: -1, y: 0};
      move();
      delete key[37];
    }
  }

  if (person.positionMap.c > 0) {
    if (38 in key) {
      person.direction = {x: 0, y: -1};
      move();
      delete key[38];
    }
  }
  
  if (person.positionMap.r < 15) {
    if (39 in key) {
      person.direction = {x: 1, y: 0};
      move();
      delete key[39];
    }
  }
  
  if (person.positionMap.c < 15) {
    if (40 in key) {
      person.direction = {x: 0, y: 1};
      move();
      delete key[40];
    }
  }
  
};

// 渲染对象
var render = function(){
  // ctx.clearRect(0,0,CANVAS_WIDTH,CANVAS_HEIGHT);
  if (personReady && boxReady && boxOkReady) {
    createMap();
    ctx.drawImage(personImage, 0,0,165,165, personPosition.x, personPosition.y, STEP, STEP);

    if (mapData[box.positionMap.r][box.positionMap.c] == 4) {
      ctx.drawImage(boxOkImage, 0,0,190,190, boxPosition.x, boxPosition.y, STEP, STEP);
    }
    else {
      ctx.drawImage(boxImage, 0,0,190,190, boxPosition.x, boxPosition.y, STEP, STEP);
    }
    
  }

};


// 主循环
var main = function(){
  personPosition = convertToPosition(person);
  boxPosition = convertToPosition(box);

  update();
  render();
};

reset();
setInterval(main, 1);