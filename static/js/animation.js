var xMouse = 0;
var yMouse = 0;
var xIcon = 0;
var yIcon = 0;

function changeIcon() {
    var elem = document.getElementById("myIcon");
    elem.className = "fa fa-heart";
}

function myMove() {
    var elem = document.getElementById("myAnimation");
    var pos = 0;
    //var id = setInterval(frame, 50);
    var id2 = setInterval(getCoords, 50);
    var id3 = setInterval(followMouse, 50);

    function frame() {
        if (pos == 350) {
            clearInterval(id);
        } else {
            pos++;
            elem.style.top = pos + 'px';
            elem.style.left = pos + 'px';
        }
    }

    function followMouse() {
        //get mouse position
        //get icon position
        //move icon closer to mouse
        //icon coords plus 1 up to mouse coords
        //have if icon coords == mouse coords clear interval
        //if xMouse and yMouse = 0 dont do anything
        if (xMouse == 0 && yMouse == 0) {
            return;
        }

        if (xIcon == xMouse && yIcon == yMouse) {
            clearInterval(id3);
        }

        //if mouse is above icon
        if (yMouse - yIcon < 0) {
            elem.style.top = --yIcon + 'px';
        }
        //if mouse is below icon
        else if (yMouse - yIcon > 0) {
            elem.style.top = ++yIcon + 'px';
        }
        //if mouse is right of icon
        if (xMouse - xIcon > 0) {
            elem.style.left = ++xIcon + 'px';
        }
        // if mouse is left of icon
        else if (xMouse - xIcon < 0) {
            elem.style.left = --xIcon + 'px';
        }

    }

    function getCoords() {
        //yIcon starts at 101 due to position of box on page
        //maths won't work unless lowest value yIcon can be is zero
        //minus 101 from yIcon
        var rect = elem.getBoundingClientRect();
        console.log(rect.top, rect.right, rect.bottom, rect.left);
        xIcon = rect.left;
        yIcon = rect.top - 101;
        var coords = "X coords: " + xIcon + ", Y coords: " + yIcon;
        document.getElementById("demo1").innerHTML = coords;
    }
}

function trackMouse() {
    //yMouse starts at 101 due to position of box on page
    //maths won't work unless lowest value yMouse can be is zero
    //minus 101 from yMouse
    xMouse = event.clientX;
    yMouse = event.clientY - 101;
    var coords = "X coords: " + xMouse + ", Y coords: " + yMouse;
    document.getElementById("demo").innerHTML = coords;

}

//function TrackIcon() {
    //var elem = document.getElementById("myAnimation");
   	//var x = event.clientX;
   	//var y = event.clientY;
    //var coords = "X coords: " + x + ", Y coords: " + y;
    //document.getElementById("demo1").innerHTML = coords;
    //}

//}

window.onload = function() {
    myMove();
};

