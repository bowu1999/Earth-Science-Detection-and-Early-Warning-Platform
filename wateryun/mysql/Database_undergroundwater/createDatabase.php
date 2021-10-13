<?php
$servername = "localhost";
$username = "root";
$password = "Wb,123456";
 
// 创建连接
$conn = new mysqli($servername, $username, $password);
 
// 检测连接
if ($conn->connect_error) {
    die("连接失败:\n " . $conn->connect_error);
} 
echo "连接成功\n";

$sql = "CREATE DATABASE Database_undergroundwater";
if ($conn->query($sql) === TRUE) {
    echo "数据库创建成功\n";
} else {
    echo "Error creating database:\n " . $conn->error;
}
$conn->close();
echo "连接关闭\n";
?>

