'Lookup -  search for numbers among 100-500++ files in a folder

num= InputBox("Please enter the number","Look for")
Set result Set fldr = fso.GetFolder(folderpath)
Set fls = fldr.Files
Set d=CreateObject("Scripting.Dictionary")
n=1

For Each fl In fls
Set r= fl.OpenAsTextStream(1)
content = r.ReadAll
if instr(1,content,num) then
d.Add "a" & n, fl.name
n=n+1
end if
r.close

Next
allRslt=d.Items
counter=d.Count

set w= result.CreateTextFile("result.txt") 'put all the result into this file, just in case it appears in multiple files
if counter>0 then
For i=0 to counter-1
w.WriteLine allRslt(i)
Next
end if
w.close