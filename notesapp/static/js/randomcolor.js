function pickColor() {

            // Array containing colors
            var colors = [
                '#25C7D8', '#EB5F9E', '#81C52C',
            ];

            // selecting random color
            var random_color = colors[Math.floor(
                    Math.random() * colors.length)];

            var notes = document.getElementsByClassName('note');
            for ( let note of notes)
            {
                    note.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            }
        }