<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Bundle of Joy</title>
    <style>
        /* Basic CSS for styling */
        body { font-family: sans-serif; }
        .button { padding: 10px 20px; cursor: pointer; }
        .image-gallery img { max-width: 100%; height: auto; display: none; }
        .image-gallery img.active { display: block; }
        .tab-container .tab-content { display: none; border: 1px solid #ccc; padding: 15px; }
        .tab-container .tab-content.active { display: block; }
        .accordion-item .accordion-content { display: none; padding: 10px; border: 1px solid #eee; }
        .accordion-item.active .accordion-content { display: block; }
        .error { color: red; font-size: 0.8em; }
    </style>
</head>
<body>

    <h1>Welcome to Your Interactive Bundle of Joy!</h1>

    <section>
        <h2>1. Event Handling</h2>
        <button id="clickButton" class="button">Click Me!</button>
        <div id="hoverArea" style="background-color: lightblue; padding: 20px;">Hover Over Me</div>
        <input type="text" id="keypressInput" placeholder="Type something here">
        <p id="keypressOutput"></p>
        <button id="doubleClickButton" class="button">Double Click (or Long Press) Me for a Surprise!</button>
        <p id="secretAction"></p>
    </section>

    <section>
        <h2>2. Interactive Elements</h2>
        <button id="colorTextButton" class="button">Change Text/Color</button>
        <p id="changingText">This text will change!</p>

        <div class="image-gallery">
            <img src="image1.jpg" alt="Image 1" class="active">
            <img src="image2.jpg" alt="Image 2">
            <img src="image3.jpg" alt="Image 3">
            <button id="prevImage">Previous</button>
            <button id="nextImage">Next</button>
        </div>

        <div class="tab-container">
            <div class="tabs">
                <button class="tab-button" data-tab="tab1">Tab 1</button>
                <button class="tab-button" data-tab="tab2">Tab 2</button>
                <button class="tab-button" data-tab="tab3">Tab 3</button>
            </div>
            <div id="tab1" class="tab-content active">Content for Tab 1</div>
            <div id="tab2" class="tab-content">Content for Tab 2</div>
            <div id="tab3" class="tab-content">Content for Tab 3</div>
        </div>

        <div class="accordion">
            <div class="accordion-item">
                <button class="accordion-header">Section 1</button>
                <div class="accordion-content">Content for Section 1</div>
            </div>
            <div class="accordion-item">
                <button class="accordion-header">Section 2</button>
                <div class="accordion-content">Content for Section 2</div>
            </div>
        </div>

        <div id="animatedElement" style="width: 100px; height: 100px; background-color: red; position: relative;">Animate Me!</div>
    </section>

    <section>
        <h2>3. Form Validation</h2>
        <form id="myForm">
            <div>
                <label for="name">Name:</label>
                <input type="text" id="name" required>
                <p id="nameError" class="error"></p>
            </div>
            <div>
                <label for="email">Email:</label>
                <input type="email" id="email" required>
                <p id="emailError" class="error"></p>
            </div>
            <div>
                <label for="password">Password:</label>
                <input type="password" id="password" required>
                <p id="passwordError" class="error"></p>
            </div>
            <button type="submit">Submit</button>
            <p id="formMessage"></p>
        </form>
    </section>

    <script>
        // JavaScript to handle the interactions

        // 1. Event Handling
        const clickButton = document.getElementById('clickButton');
        const hoverArea = document.getElementById('hoverArea');
        const keypressInput = document.getElementById('keypressInput');
        const keypressOutput = document.getElementById('keypressOutput');
        const doubleClickButton = document.getElementById('doubleClickButton');
        const secretAction = document.getElementById('secretAction');

        clickButton.addEventListener('click', () => {
            alert('Button Clicked!');
        });

        hoverArea.addEventListener('mouseover', () => {
            hoverArea.style.backgroundColor = 'yellow';
        });

        hoverArea.addEventListener('mouseout', () => {
            hoverArea.style.backgroundColor = 'lightblue';
        });

        keypressInput.addEventListener('keyup', (event) => {
            keypressOutput.textContent = You typed: ${event.key};
        });

        let clickCount = 0;
        let timer;
        doubleClickButton.addEventListener('click', () => {
            clickCount++;
            if (clickCount === 1) {
                timer = setTimeout(() => {
                    secretAction.textContent = 'Long press detected!';
                    clickCount = 0;
                }, 500); // Adjust time for long press
            } else if (clickCount === 2) {
                clearTimeout(timer);
                secretAction.textContent = 'Double click detected! Here's a ✨ surprise! ✨';
                clickCount = 0;
            }
        });

        // 2. Interactive Elements
        const colorTextButton = document.getElementById('colorTextButton');
        const changingText = document.getElementById('changingText');
        const colors = ['red', 'green', 'blue', 'purple'];
        let colorIndex = 0;

        colorTextButton.addEventListener('click', () => {
            changingText.style.color = colors[colorIndex];
            changingText.textContent = Now it's ${colors[colorIndex]}!;
            colorIndex = (colorIndex + 1) % colors.length;
        });

        const images = document.querySelectorAll('.image-gallery img');
        const prevButton = document.getElementById('prevImage');
        const nextButton = document.getElementById('nextImage');
        let imageIndex = 0;

        function showImage(index) {
            images.forEach(img => img.classList.remove('active'));
            images[index].classList.add('active');
        }

        prevButton.addEventListener('click', () => {
            imageIndex = (imageIndex - 1 + images.length) % images.length;
            showImage(imageIndex);
        });

        nextButton.addEventListener('click', () => {
            imageIndex = (imageIndex + 1) % images.length;
            showImage(imageIndex);
        });

        const tabButtons = document.querySelectorAll('.tab-button');
        const tabContents = document.querySelectorAll('.tab-content');

        tabButtons.forEach(button => {
            button.addEventListener('click', () => {
                const tabId = button.getAttribute('data-tab');
                tabButtons.forEach(btn => btn.classList.remove('active'));
                tabContents.forEach(content => content.classList.remove('active'));
                button.classList.add('active');
                document.getElementById(tabId).classList.add('active');
            });
        });

        const accordionHeaders = document.querySelectorAll('.accordion-header');
        accordionHeaders.forEach(header => {
            header.addEventListener('click', () => {
                const accordionItem = header.parentNode;
                accordionItem.classList.toggle('active');
            });
        });

        const animatedElement = document.getElementById('animatedElement');
        let position = 0;
        setInterval(() => {
            position = (position + 5) % 200;
            animatedElement.style.left = ${position}px;
        }, 50);

        // 3. Form Validation
        const form = document.getElementById('myForm');
        const nameInput = document.getElementById('name');
        const emailInput = document.getElementById('email');
        const passwordInput = document.getElementById('password');
        const nameError = document.getElementById('nameError');
        const emailError = document.getElementById('emailError');
        const passwordError = document.getElementById('passwordError');
        const formMessage = document.getElementById('formMessage');

        form.addEventListener('submit', (event) => {
            let isValid = true;

            if (!nameInput.value.trim()) {
                nameError.textContent = 'Name is required';
                isValid = false;
            } else {
                nameError.textContent = '';
            }

            if (!emailInput.value.trim()) {
                emailError.textContent = 'Email is required';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value)) {
                emailError.textContent = 'Invalid email format';
                isValid = false;
            } else {
                emailError.textContent = '';
            }

            if (!passwordInput.value) {
                passwordError.textContent = 'Password is required';
                isValid = false;
            } else if (passwordInput.value.length < 8) {
                passwordError.textContent = 'Password must be at least 8 characters long';
                isValid = false;
            } else {
                passwordError.textContent = '';
            }

            if (!isValid) {
                event.preventDefault(); // Prevent form submission if validation fails
                formMessage.textContent = '';
            } else {
                formMessage.textContent = 'Form submitted successfully!';
                // In a real scenario, you would submit the form data here
            }
        });

        // Real-time feedback for password
        passwordInput.addEventListener('input', () => {
            if (passwordInput.value.length < 8) {
                passwordError.textContent = 'Password must be at least 8 characters long';
            } else {
                passwordError.textContent = '';
            }
        });
    </script>

</body>
</html>