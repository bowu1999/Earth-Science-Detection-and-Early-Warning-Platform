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
$sql = "CREATE TABLE Table_devices (
id CHAR(20) NOT NULL PRIMARY KEY  COMMENT '设备号', 
longitude CHAR(20) NOT NULL COMMENT '经度',
latitude CHAR(20) NOT NULL COMMENT '纬度',
state CHAR(10) NOT NULL COMMENT '状态',
number CHAR(20) NOT NULL COMMENT '物联网卡号',
renew_date DATE NOT NULL COMMENT '续费日期',
expire_date DATE NOT NULL COMMENT '到期日期'
)";
 
if ($conn->query($sql) === TRUE) {
    echo "Table MyGuests created successfully\n";
} else {
    echo "创建数据表错误: \n" . $conn->error;
}

$conn->close();
echo "连接关闭\n";
?>

