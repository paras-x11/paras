<?php
include '../components/connected.php';

if (isset($_COOKIE['seller_id'])) {
    $seller_id = $_COOKIE['seller_id'];
} else {
    header('Location: login.php');
    exit();
}

// Fetch active and deactive products for this seller
$select_active_products = $conn->prepare("SELECT * FROM `products` WHERE seller_id = ? AND status = 'active'");
$select_active_products->execute([$seller_id]);
$active_products = $select_active_products->fetchAll(PDO::FETCH_ASSOC);

$select_deactive_products = $conn->prepare("SELECT * FROM `products` WHERE seller_id = ? AND status = 'deactive'");
$select_deactive_products->execute([$seller_id]);
$deactive_products = $select_deactive_products->fetchAll(PDO::FETCH_ASSOC);

?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>View Products - Admin Dashboard</title>
    <link rel="stylesheet" type="text/css" href="../css/admin_style.css">
</head>
<body>
    <div class="main-container">
        <?php include '../components/admin_header.php'; ?>

        <section class="view-products">
            <div class="heading">
                <h1>Active Products</h1>
            </div>
            <div class="product-container">
                <?php if (count($active_products) > 0): ?>
                    <?php foreach ($active_products as $product): ?>
                        <div class="product-box">
                            <img src="<?= $product['image']; ?>" alt="<?= $product['name']; ?>">
                            <h3><?= htmlspecialchars($product['name']); ?></h3>
                            <p><?= htmlspecialchars($product['description']); ?></p>
                            <p>Price: $<?= htmlspecialchars($product['price']); ?></p>
                            <p>Status: <?= htmlspecialchars($product['status']); ?></p>
                            <a href="update_product.php?id=<?= $product['id']; ?>" class="btn">Update</a>
                        </div>
                    <?php endforeach; ?>
                <?php else: ?>
                    <p>No active products found.</p>
                <?php endif; ?>
            </div>

            <div class="heading">
                <h1>Deactive Products</h1>
            </div>
            <div class="product-container">
                <?php if (count($deactive_products) > 0): ?>
                    <?php foreach ($deactive_products as $product): ?>
                        <div class="product-box">
                            <img src="<?= $product['image']; ?>" alt="<?= $product['name']; ?>">
                            <h3><?= htmlspecialchars($product['name']); ?></h3>
                            <p><?= htmlspecialchars($product['description']); ?></p>
                            <p>Price: $<?= htmlspecialchars($product['price']); ?></p>
                            <p>Status: <?= htmlspecialchars($product['status']); ?></p>
                            <a href="update_product.php?id=<?= $product['id']; ?>" class="btn">Update</a>
                        </div>
                    <?php endforeach; ?>
                <?php else: ?>
                    <p>No deactive products found.</p>
                <?php endif; ?>
            </div>
        </section>
    </div>
</body>
</html>
