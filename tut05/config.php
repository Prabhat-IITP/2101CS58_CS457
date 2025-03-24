<?php
$host = 'localhost';
$dbname = 'cs457_lab5';
$username = 'cs457_lab5';
$password = 'cs457_lab5'; // Update with your MySQL password

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}
?>
