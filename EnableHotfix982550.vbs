Const SE_VPS_GUID = "{143F5698-103B-12D4-FF34-1F34767DEabc}"
Const SE_VPS_NAME = "EnableHotfix982550"
Const SE_VPS_VALUE = true

Sub SetValue()

    ' Create the root object.
    Dim root  ' The FPCLib.FPC root object
    Set root = CreateObject("FPC.Root")

    'Declare the other objects that are needed.
    Dim array       ' An FPCArray object
    Dim VendorSets  ' An FPCVendorParametersSets collection
    Dim VendorSet   ' An FPCVendorParametersSet object

    ' Get references to the array object
    ' and the network rules collection.
    Set array = root.GetContainingArray
    Set VendorSets = array.VendorParametersSets

    On Error Resume Next
    Set VendorSet = VendorSets.Item( SE_VPS_GUID )

    If Err.Number <> 0 Then
        Err.Clear

        ' Add the item
        Set VendorSet = VendorSets.Add( SE_VPS_GUID )
        CheckError
        WScript.Echo "New VendorSet added... " & VendorSet.Name

    Else
        WScript.Echo "Existing VendorSet found... value- " &  VendorSet.Value(SE_VPS_NAME)
    End If

    if VendorSet.Value(SE_VPS_NAME) <> SE_VPS_VALUE Then

        Err.Clear
        VendorSet.Value(SE_VPS_NAME) = SE_VPS_VALUE

        If Err.Number <> 0 Then
            CheckError
        Else
            VendorSets.Save false, true
            CheckError

            If Err.Number = 0 Then
                WScript.Echo "Done with " & SE_VPS_NAME & ", saved!"
            End If
        End If
    Else
        WScript.Echo "Done with " & SE_VPS_NAME & ", no change!"
    End If

End Sub

Sub CheckError()

    If Err.Number <> 0 Then
        WScript.Echo "An error occurred: 0x" & Hex(Err.Number) & " " & Err.Description
        Err.Clear
    End If

End Sub

SetValue