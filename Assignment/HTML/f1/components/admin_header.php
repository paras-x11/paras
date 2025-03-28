<?php
session_start();
include '../components/connected.php';

// Check if the seller is logged in by verifying session data
if (isset($_SESSION['seller_id'])) {
    $seller_id = $_SESSION['seller_id']; // Retrieve seller_id from session
} else {
    // Redirect to login page if not logged in
    header("Location: login.php");
    exit();
}

// Handle login request
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL); // Sanitize email
    $password = $_POST['password']; // Don't hash password yet

    // Prepare query to check if email and password match
    $query = $conn->prepare("SELECT * FROM `sellers` WHERE email = ?");
    $query->execute([$email]);

    if ($query->rowCount() > 0) {
        $seller = $query->fetch(PDO::FETCH_ASSOC);
        
        // Verify the password with password_verify
        if (password_verify($password, $seller['password'])) {
            $_SESSION['seller_id'] = $seller['id']; // Store seller_id in the session
            header("Location: dashboard.php");
            exit();
        } else {
            echo "Invalid email or password.";
        }
    } else {
        echo "Invalid email or password.";
    }
}
?>

<header>
    <div class="logo">
        <img src="https://logos-world.net/wp-content/uploads/2023/12/Formula-One-Logo-1994-500x281.png" width="200">
    </div>
    <div class="right">
        <div class="bx bxs-user" id="user-btn"></div>
        <div class="toggle-btn"><i class="bx bx-menu"></i></div>
    </div>
    <div class="profile-detail">
        <?php
        // Fetch seller profile details
        $select_profile = $conn->prepare("SELECT * FROM `sellers` WHERE id = ?");
        $select_profile->execute([$seller_id]);

        if ($select_profile->rowCount() > 0) {
            $fetch_profile = $select_profile->fetch(PDO::FETCH_ASSOC);
        ?>
        <div class="profile">
            <img src="../uploaded_files/<?= htmlspecialchars($fetch_profile['image']); ?>" class="logo-img" width="150">
            <p><?= htmlspecialchars($fetch_profile['name']); ?></p>
            <div class="flex-btn">
                <a href="profile.php" class="btn">profile</a>
                <a href="../components/admin_logout.php" onclick="return confirm('Logout from this website?');" class="btn">logout</a>
            </div>
        </div>
        <?php } ?>
    </div>
</header>

<div class="sidebar-container">
    <div class="sidebar">
        <?php
        // Fetch the seller profile details for the sidebar
        $select_profile = $conn->prepare("SELECT * FROM `sellers` WHERE id = ?");
        $select_profile->execute([$seller_id]);

        if ($select_profile->rowCount() > 0) {
            $fetch_profile = $select_profile->fetch(PDO::FETCH_ASSOC);
        ?>
        <div class="profile">
            <img src="../uploaded_files/<?= htmlspecialchars($fetch_profile['image']); ?>" class="logo-img" width="100">
            <p><?= htmlspecialchars($fetch_profile['name']); ?></p>
        </div>
        <?php } ?>
        <h5>menu</h5>
        <div class="navbar">
            <ul>
                <li> <a href="dashboard.php"><i class="bx bxs-home-smile"></i>dashboard</a></li>
                <li> <a href="add_product.php"><i class="bx bxs-shopping-bags"></i>add product</a></li>
                <li> <a href="view_product.php"><i class="bx bxs-food-menu"></i>view product</a></li>
                <li> <a href="user_accounts.php"><i class="bx bxs-user_detail"></i>account</a></li>
                <li> <a href="../components/admin_logout.php" onclick="return confirm('Logout from this website?');"><i class="bx bxs-log-out"></i>logout</a></li>
            </ul>
        </div><br><br><br><center>
    <div class="social-links">
        <a href="https://facebook.com" target="_blank"><img src="https://freepnglogo.com/images/all_img/1713419302Black_Facebook_PNG.png" alt="Facebook" width="25"></a>
        <a href="https://instagram.com" target="_blank"><img src="https://freepnglogo.com/images/all_img/1715966613instagram-logo-black-and-white-png.png" alt="Instagram" width="25"></a>
        <a href="https://linkedin.com" target="_blank"><img src="https://tse1.mm.bing.net/th?id=OIP.MaqcSfiMThZuoDpaYYsSMgHaHa&pid=Api&P=0&h=180" alt="LinkedIn" width="25"></a>
        <a href="https://twitter.com" target="_blank"><img src="https://freepnglogo.com/images/all_img/1707226109new-twitter-logo-png.png" alt="Twitter" width="25"></a>
       <a href="https://pinterest.com" target="_blank"><img src="https://pnggrid.com/wp-content/uploads/2024/11/Black-Pinterest-Logo-1024x1024.png" alt="Pinterest" width="25"></a>
    </div>
    </center>
    </div>
</div>
