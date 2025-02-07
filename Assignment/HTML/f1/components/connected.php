<?php
// Database connection details
$db_host = '127.0.0.1'; // Use '127.0.0.1' to avoid potential hostname issues
$db_name = 'f1_db';
$db_user = 'root';
$db_password = 'root1'; // Update with your password if not empty

try {
    // Connect to the database using PDO
    $conn = new PDO("mysql:host=$db_host;dbname=$db_name;charset=utf8", $db_user, $db_password);
    // Set PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully!";
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

// Function to generate a unique ID
if (!function_exists('unique_id')) {
    function unique_id() {
        $chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
        $charsLength = strlen($chars);
        $randomString = '';
        for ($i = 0; $i < 20; $i++) {
            $randomString .= $chars[mt_rand(0, $charsLength - 1)];
        }
        return $randomString;
    }
}
?>
