function pickColor() {

            // Array containing colors
            var colors = [
                '#25C7D8', '#EB5F9E', '#81C52C',
            ];

            // selecting random color
            var random_color = colors[Math.floor(
                    Math.random() * colors.length)];

            var uforms = document.getElementsByClassName('updateform');
            for ( uform  of uforms)
            {
                    uform.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            }
        }