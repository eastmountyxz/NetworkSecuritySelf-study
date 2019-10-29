foreach ($file in dir c:\python34)
{
    if($file.length -gt 1kb)
    {
        $file.name
        $file.length
    }
}
