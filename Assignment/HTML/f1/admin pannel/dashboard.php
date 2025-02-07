<?php
include '../components/connected.php';

if (isset($_COOKIE['seller_id'])) {
    $seller_id = $_COOKIE['seller_id'];
} else {
    $seller_id = '';
    header('Location: login.php');
    exit();
}

// Fetch seller profile
$select_profile = $conn->prepare("SELECT * FROM `sellers` WHERE id = ?");
$select_profile->execute([$seller_id]);
$fetch_profile = $select_profile->fetch(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Formula 1 - Admin Dashboard page</title>
    <link rel="stylesheet" type="text/css" href="../css/admin_style.css">
    <!-- Font awesome and box icon CDN links -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">
</head>
<body>

<div class="main-container">
    <?php include '../components/admin_header.php'; ?>
    <section class="dashboard">
        <div class="heading">
            <h1>Dashboard</h1>
            <img src="https://tse4.mm.bing.net/th?id=OIP.zgnLbe1w5yJKtr-_Nbf-hwHaHa&pid=Api&P=0&h=180">
        </div> 
        <div class="box-container">
            <div class="box">
                <h3>Welcome!</h3>
                <p><?= htmlspecialchars($fetch_profile['name']); ?></p>
                <a href="update.php" class="btn">Update Profile</a>
            </div>

            <!-- Unread messages -->
            <div class="box">
                <?php
                    $select_message = $conn->prepare("SELECT * FROM `message`");
                    $select_message->execute();
                    $number_of_msg = $select_message->rowCount();
                ?>
                <h3><?= $number_of_msg; ?></h3>
                <p>Unread Message</p>
                <a href="admin_message.php" class="btn">See Message</a>
            </div>

            <!-- Products added -->
            <div class="box">
                <?php
                    $select_products = $conn->prepare("SELECT * FROM `products` WHERE seller_id = ?");
                    $select_products->execute([$seller_id]);
                    $number_of_products = $select_products->rowCount();
                ?>
                <h3><?= $number_of_products; ?> </h3>
                <p>Products Added</p>
                <a href="add_product.php" class="btn">Add Product</a>
            </div>

            <!-- Active products -->
            <div class="box">
                <?php
                    $select_active_products = $conn->prepare("SELECT * FROM `products` WHERE seller_id = ? AND status = 'active'");
                    $select_active_products->execute([$seller_id]);
                    $number_of_active_products = $select_active_products->rowCount();
                ?>
                <h3><?= $number_of_active_products; ?> </h3>
                <p>Total Active Products</p>
                <a href="view_product.php" class="btn">Active Products</a>
            </div>

            <!-- Deactive products -->
            <div class="box">
                <?php
                    $select_deactive_products = $conn->prepare("SELECT * FROM `products` WHERE seller_id = ? AND status = 'deactive'");
                    $select_deactive_products->execute([$seller_id]);
                    $number_of_deactive_products = $select_deactive_products->rowCount();
                ?>
                <h3><?= $number_of_deactive_products; ?> </h3>
                <p>Total Deactive Products</p>
                <a href="view_product.php" class="btn">Deactive Products</a>
            </div>

            <!-- Users account -->
            <div class="box">
                <?php
                    $select_users = $conn->prepare("SELECT * FROM `users`");
                    $select_users->execute();
                    $number_of_users = $select_users->rowCount();
                ?>
                <h3><?= $number_of_users; ?></h3>
                <p>Users Account</p>
                <a href="user_accounts.php" class="btn">See Users</a>
            </div>

            <!-- Sellers account -->
            <div class="box">
                <?php
                    $select_sellers = $conn->prepare("SELECT * FROM `sellers`");
                    $select_sellers->execute();
                    $number_of_sellers = $select_sellers->rowCount();
                ?>
                <h3><?= $number_of_sellers; ?></h3>
                <p>Sellers Account</p>
                <a href="user_accounts.php" class="btn">See Sellers</a>
            </div>

            <!-- Orders -->
            <div class="box">
                <?php
                    $select_orders = $conn->prepare("SELECT * FROM `orders` WHERE seller_id = ?");
                    $select_orders->execute([$seller_id]);
                    $number_of_orders = $select_orders->rowCount();
                ?>
                <h3><?= $number_of_orders; ?></h3>
                <p>Total Orders Placed</p>
                <a href="admin_order.php" class="btn">Total Orders</a>
            </div>

            <!-- Confirm orders -->
            <div class="box">
                <?php
                    $select_confirm_orders = $conn->prepare("SELECT * FROM `orders` WHERE seller_id = ? AND status = 'in progress'");
                    $select_confirm_orders->execute([$seller_id]);
                    $number_of_confirm_orders = $select_confirm_orders->rowCount();
                ?>
                <h3><?= $number_of_confirm_orders; ?></h3>
                <p>Total Confirm Orders</p>
                <a href="admin_order.php" class="btn">Confirm Orders</a>
            </div>

            <!-- Canceled orders -->
            <div class="box">
                <?php
                    $select_canceled_orders = $conn->prepare("SELECT * FROM `orders` WHERE seller_id = ? AND status = 'in canceled'");
                    $select_canceled_orders->execute([$seller_id]);
                    $number_of_canceled_orders = $select_canceled_orders->rowCount();
                ?>
                <h3><?= $number_of_canceled_orders; ?></h3>
                <p>Total Canceled Orders</p>
                <a href="admin_order.php" class="btn">Canceled Orders</a>
            </div>
        </div>
    </section>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/sweetalert/2.1.2/sweetalert.min.js"></script>
<script src="../js/admin_script.js"></script>
<?php include '../components/alert.php'; ?>
</body>
</html>
