<?php

require_once __DIR__.'/include/Database.php';

$host = getenv('DB_HOST') ?: '192.168.10.101';
$port = getenv('DB_PORT') ?: '3306';
$db   = getenv('DB_NAME') ?: 'cliente';
$user = getenv('DB_USER') ?: 'crud';
$pass = getenv('DB_PASS') ?: '9kjThhnVcXJP';

$dsn = "mysql:host={$host};port={$port};dbname={$db};charset=utf8mb4";

$opts = [
  PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
  PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
  PDO::ATTR_EMULATE_PREPARES   => false,
];

$pdo = new PDO($dsn, $user, $pass, $opts);

// IMPORTANTe: passe o PDO para seu wrapper Database
$db = new Database($pdo);

?>
