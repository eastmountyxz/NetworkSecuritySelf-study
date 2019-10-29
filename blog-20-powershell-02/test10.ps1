$num=1..10
switch($num)
{
    default{"number=$_"}
}

$num=1..10
switch($num)
{
    {($_ % 2) -eq 0} {"$_ 数值是偶数"}
    {($_ % 2) -ne 0} {"$_ 数值是奇数"}
}