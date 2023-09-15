<?php
$selectedValue = $_GET["selectedValue"];
$folderPath = "D:/360MoveData/Users/叶子呢/Desktop/录屏集合/num2/timu-50";

// 获取文件夹中的所有文件
$files = scandir($folderPath);

// 过滤出匹配的标题名称
$searchResults = array();
foreach ($files as $file) {
    if ($file !== "." && $file !== "..") {
        $content = file_get_contents($folderPath . "/" . $file);
        if (strpos($content, $selectedValue) !== false) {
            $searchResults[] = $file;
        }
    }
}

// 返回搜索结果
echo json_encode($searchResults);
?>