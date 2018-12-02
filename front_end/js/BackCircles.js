const canvas = document.querySelector(".anime");
const c = canvas.getContext("2d");

function setCanvasSize() {
	canvas.height = window.innerHeight;
	canvas.width = window.innerWidth;
}

let mouse = {
	x: undefined,
	y: undefined
};

class Circle {
	constructor(x, y, dx, dy, radius, color) {
		this.x = x;
		this.y = y;
		this.dx = dx;
		this.dy = dy;
		this.radius = radius;
		this.minRadius = radius;
		this.maxRadius = 40;
		this.color = color;
	}

	draw() {
		c.beginPath();
		c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
		c.fillStyle = this.color;
		c.fill();
	}

	update() {
		if (this.x + this.radius > innerWidth || this.x - this.radius < 0) {
			this.dx = -this.dx;
		}

		if (this.y + this.radius > innerHeight || this.y - this.radius < 0) {
			this.dy = -this.dy;
		}

		this.x += this.dx;
		this.y += this.dy;

		this.grow(mouse.x+15, mouse.y-50);
		this.draw();
	}

	grow(x, y) {
		if (
			x - this.x < 20 &&
			x - this.x > -20 &&
			y - this.y < 20 &&
			y - this.y > -20
		) {
			if (this.radius < this.maxRadius) {
				this.radius += 1;
			}
		} else if (this.radius > this.minRadius) {
			this.radius -= 1;
		}
	}
}

let circles = [];
let colors = [
	"36,46,96",
	"37,62,111",
	"40,80,149",
	"53,86,172",
	"254, 134, 10",
	"186, 223, 21",
	"213, 23, 23",
	"227, 25, 225"
];

function animate() {
	requestAnimationFrame(animate);
	c.clearRect(0, 0, innerWidth, innerHeight);

	for (let i = 0; i < circles.length; i++) {
		circles[i].update();
	}
}

function createCircles(count) {
	circles = [];
	for (let i = 0; i < count; i++) {
		let random = Math.random();
		let radius = Math.random() * 7 + 1;
		let x = Math.random() * (innerWidth - radius * 2) + radius;
		let y = Math.random() * (innerHeight - radius * 2) + radius;
		let dx = (random - 0.5) * 2;
		let dy = (random - 0.5) * 2;
		let alpha = 1;
		// alpha = random >= 0.85 ? random : 0.85; /* uncomment this line for transparency */
		let color = colors[Math.floor(Math.random() * colors.length)];
		let rgba = "rgba(" + color + ", " + alpha + ")";
		circles.push(new Circle(x, y, dx, dy, radius, rgba));
	}
}

function init() {
	const circleCount = 1000;
	createCircles(circleCount);
	setCanvasSize();
	animate();

	window.addEventListener("resize", function() {
		setCanvasSize();
		createCircles(circleCount);
	});
	window.addEventListener("mousemove", function(event) {
		mouse.x = event.x;
		mouse.y = event.y;
	});
	window.addEventListener("touchmove", function(event) {
		mouse.x = event.touches[0].clientX;
		mouse.y = event.touches[0].clientY;
	});
	window.addEventListener("touchend", function(event) {
		mouse.x = undefined;
		mouse.y = undefined;
	});
}

init();
