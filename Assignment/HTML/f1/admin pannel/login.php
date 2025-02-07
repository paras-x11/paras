<?php
session_start(); // Start session to handle login state
include '../components/connected.php'; // Include the database connection

if (isset($_POST['submit'])) {

    // Sanitize inputs
    $email = isset($_POST['email']) ? filter_var($_POST['email'], FILTER_SANITIZE_EMAIL) : '';
    $pass = isset($_POST['pass']) ? sha1($_POST['pass']) : '';

    // Check if user exists with the provided email and password
    $select_seller = $conn->prepare("SELECT * FROM `sellers` WHERE email = ? AND password = ?");
    $select_seller->execute([$email, $pass]);

    if ($select_seller->rowCount() > 0) {
        // User found, login successful
        $seller = $select_seller->fetch(PDO::FETCH_ASSOC);

        // Store seller ID in session
        $_SESSION['seller_id'] = $seller['id'];

        // Redirect to dashboard
        header('Location: dashboard.php');
        exit(); // Make sure no further code is executed
    } else {
        // Invalid login credentials
        $warning_msg[] = 'Invalid email or password.';
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formula 1 - Seller Login</title>
    <link rel="stylesheet" href="../css/admin_style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">
</head>
<body>
    <div class="form-container">
        <form action="" method="POST" class="register">
            <h3>Login Now</h3>

            <div class="flex">
                <div class="input-field">
                    <p>Your email <span>*</span></p>
                    <input type="email" name="email" placeholder="Enter your email" maxlength="50" required class="box">
                </div>
            </div>

            <div class="col">
                <div class="input-field">
                    <p>Your password <span>*</span></p>
                    <input type="password" name="pass" placeholder="Enter your password" maxlength="50" required class="box">
                </div>
            </div>

            <p class="link">Don't have an account? <a href="register.php">Register now</a></p>

            <input type="submit" name="submit" value="Login Now" class="btn">
        </form>
    </div>

    <!-- Success/Warning Messages -->
    <?php if (isset($warning_msg) && !empty($warning_msg)) { ?>
        <script>
            <?php foreach ($warning_msg as $msg) { ?>
                swal("Warning!", "<?php echo $msg; ?>", "warning");
            <?php } ?>
        </script>
    <?php } ?>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/sweetalert/2.1.2/sweetalert.min.js"></script>
    <script src="../js/script.js"></script>

    <?php include '../components/alert.php'; ?>
</body>
</html>
