set ws=createobject("wscript.shell")

sub shutfun(s)
select case s
case 1
ws.run"cmd.exe /c shutdown -s -t 300"
case 2
ws.run"cmd.exe /c shutdown -a"
end select
end sub

call shutfun(1)
do while a<>"我喜欢猪"
a=inputbox("你喜欢娜女神还是猪,快在对话框中输入喜欢猪,否则后果自负，快输""我喜欢猪"" ","输不输","")
loop
msgbox "早说就行了嘛"
msgbox"再输一遍我是猪!"
msgbox"我是猪!"
MsgBox"最后一次!"
MsgBox"如果你很快的点过去,不看的话"
MsgBox"我就要你踩我空间的!哼!"
MsgBox"从前有座山!"
MsgBox"山里有个庙."
MsgBox"庙里有个老和尚在讲故事."
ws.run"iexplore.exe https://blog.csdn.net/Eastmount"
msgbox"哎呀累了！数绵羊哄我睡觉"
for i=1 to 20
MsgBox i&"只绵羊"
next
msgbox"哎呀我困了，这次就饶过你吧，下次注意哦!"
msgbox"最后问个问题，我是不是大好人！"
call shutfun(2)
if inputbox("是不是","请选择","是")<>"是" then
call shutfun(1)
end if
