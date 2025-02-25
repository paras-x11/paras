

<!-- =========================================================================================================================== -->

<!-- FOR SQL DATABASE CONNECTION -->

<?php
// Start session if not already started
if (session_status() == PHP_SESSION_NONE) {
    session_start();
}

// Database credentials 
$host = 'localhost'; 
$dbname = 'f1'; 
$username = 'root'; 
$password = 'root1';
try {
    // MySQL database connect karna using PDO
    $conn = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);

    // PDO error mode ko Exception pe set karna
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // echo "MySQL database connected successfully!";
} catch (PDOException $e) {
    // Error log karna file me
    error_log("[" . date('Y-m-d H:i:s') . "] Database Connection Error: " . $e->getMessage() . "\n", 3, __DIR__ . "/../error_log.txt");

    // User-friendly message
    echo "Sorry, we are facing technical issues. Please try again later.";
    exit();
}

// Unique ID generate karne ka function
if (!function_exists('unique_id')) {
    function unique_id() {
        return bin2hex(random_bytes(16)); // Secure ID generation
    }
}
?>

<!-- =========================================================================================================================== -->
