<?php
// mysql管理员账户
$servername = "localhost";
$username = "root";
$password = "Wb,123456";
$dbname = 'Database_undergroundwater';
 
// 创建连接,连接到数据库Database_undergroundwater
$conn = new mysqli($servername, $username, $password,$dbname);
 
// 检测连接
if ($conn->connect_error) {
    die("连接失败:\n " . $conn->connect_error);
} 
echo "连接成功\n";

// 使用 sql 创建数据表
$sql = "CREATE TABLE Table_water (
id INT(20) PRIMARY KEY AUTO_INCREMENT, 
deviceID FLOAT(20),
depth FLOAT(20) NOT NULL,
conduct FLOAT(20) NOT NULL,
resistivity FLOAT(20) NOT NULL,
temperature FLOAT(20) NOT NULL,
tds FLOAT(20) NOT NULL,
salinity FLOAT(20) NOT NULL,
date_time DATETIME NOT NULL
)";
 
if ($conn->query($sql) === TRUE) {
    echo "Table MyGuests created successfully\n";
} else {
    echo "创建数据表错误: \n" . $conn->error;
}

$conn->close();
echo "连接关闭\n";
?>

