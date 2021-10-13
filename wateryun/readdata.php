<?php
$servername = "localhost";
$username = "visiter";
$password = "Allvisit_password,407";
$dbname = "Database_undergroundwater";
 
// 创建连接
$conn = new mysqli($servername, $username, $password,$dbname);
 
// 检测连接
if ($conn->connect_error) {
    die("连接失败:\n " . $conn->connect_error);
} 
// 设置编码，防止中文乱码
mysqli_set_charset($conn, "utf8");

$sql = "SELECT * FROM `Table_water` ORDER BY id DESC LIMIT 0 , 7 ";
$result = mysqli_query($conn,$sql);
if (mysqli_num_rows($result) > 0) {
    // 输出数据
    while($row = mysqli_fetch_assoc($result)) {
        echo "{$row["date_time"]} {$row["depth"]} {$row["conduct"]} {$row["resistivity"]} {$row["temperature"]} {$row["tds"]} {$row["salinity"]} ";

    }
} else {
    echo "0 结果";
}
$conn->close();
?>

