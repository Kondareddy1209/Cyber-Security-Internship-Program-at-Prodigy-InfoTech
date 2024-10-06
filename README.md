<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Font Awesome CDN for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" integrity="sha384-k6RqeWeci5ZR/Lv4MR0sA0FfDOM2f5sYz8NnYf1i2tn9r8kR5Rk4qzG4BfZ3Y7p" crossorigin="anonymous">
</head>
<body>
    <h1>
        PRODIGY CS - Task 01
    </h1>
    <p>Welcome to the <strong>PRODIGY CS - Task 01</strong> repository! This project implements encryption and decryption functionalities using the Caesar cipher technique.</p> 
    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#projects">Projects Overview</a></li>
        <li><a href="#technologies-used">Technologies Used</a></li>
        <li><a href="#getting-started">Getting Started</a></li>
        <li><a href="#usage-instructions">Usage Instructions</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
    </ul>  
    <h2 id="projects">Projects Overview</h2>
    <p>This project focuses on a simple implementation of the Caesar cipher for encrypting and decrypting messages. The implementation is available in both Python and C.</p>
    <h3>File Structure</h3>
    <ul>
        <li><strong>cisear.py</strong>: Python implementation of the Caesar cipher.</li>
        <li><strong>Task-01_Encryption_and_Decryption_in_cisear.c</strong>: C implementation of the Caesar cipher.</li>
    </ul>
    <h2 id="technologies-used">Technologies Used</h2>
    <ul>
        <li>Python</li>
    </ul>
    <h2 id="getting-started">Getting Started</h2>
    <p>To get a copy of this repository up and running on your local machine, follow these steps:</p>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/Kondareddy1209/PRODIGY-CS-01-Task--01.git</code></pre>
        </li>
        <li>Navigate to the project directory:
            <pre><code>cd PRODIGY-CS-01-Task--01</code></pre>
        </li>
        <li>Run the Python script to perform encryption and decryption:
            <pre><code>python cisear.py</code></pre>
        </li>
    </ol>
    <h2 id="usage-instructions">Usage Instructions</h2>
    <p>The following functions are implemented in the Python script:</p>
    <ul>
        <li><strong>encrypt(plaintext, shift)</strong>: Encrypts the given plaintext using a specified shift value.</li>
        <li><strong>decrypt(ciphertext, shift)</strong>: Decrypts the given ciphertext using the specified shift value.</li>
    </ul>
    <h3>Example Usage</h3>
    <pre><code>shift_value = 3  # Set your desired shift value
original_text = "Hello, World!"
encrypted = encrypt(original_text, shift_value)
decrypted = decrypt(encrypted, shift_value)

print(f"Original: {original_text}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")</code></pre>
    <h2 id="contributing">Contributing</h2>
    <p>Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and create a pull request.</p>
    <h2 id="license">License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
    <h2>🤳 Connect with Me:</h2>
    <a href="https://www.linkedin.com/in/ambavaram-tirumala-kondareddy-b68851275/" target="_blank" aria-label="LinkedIn">
      <img align="left" alt="Kondareddy | LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
    </a>
    <a href="https://www.instagram.com/mr_konda_reddy.c_18/" target="_blank" aria-label="Instagram">
      <img align="left" alt="Kondareddy | Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />
    </a>
    <a href="https://github.com/Kondareddy1209" target="_blank" aria-label="GitHub">
      <img align="left" alt="Kondareddy | GitHub" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg" />
    </a>
    <a href="https://kondareddy1209.github.io/" target="_blank" aria-label="Portfolio">
      <i class="fa-solid fa-briefcase" style="font-size: 22px; margin-right: 5px;"></i>
      <span>My Portfolio</span>
    </a>
    <br/>
    <p>Feel free to reach out for any questions or collaborations!</p>
</body>
</html>
