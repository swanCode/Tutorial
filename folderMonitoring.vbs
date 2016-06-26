'Any files that stay more that 30 minutes is consider an alert and it needs to be taken care of and the alert will be sent through email.

age_threshold = 30 'in minutes

folderPath = "path"

Set fso = CreateObject("Scripting.FileSystemObject")
Set fldr = fso.getFolder(folderPath )

file_found = 0

Set shell = wscript.CreateObject("Shell.Application")

For Each fl in fldr.Files
age = DateDiff("n", fl .DateCreated, Now) 'DateCreated is the date that it is put in to the folder instead of using DateLastModified
If age > age_threshold Then
file_found = file_found+1
End If
Next
if file_found > 0 then
sendAlert(file_found)
WScript.Quit()
else
WScript.Quit()
end if

sub sendAlert(no)
Set objOutlook = CreateObject("Outlook.Application")
Set objMail = objOutlook.CreateItem(0)
objMail.Display 'To display message
objMail.To = "xyz@xyz.com"
objMail.Subject = "Alert: Folder XYZ"
objMail.Body = "Please check the XYZ folder - "&folderPath
objMail.Send
Set objMail = Nothing
Set objOutlook = Nothing
end sub