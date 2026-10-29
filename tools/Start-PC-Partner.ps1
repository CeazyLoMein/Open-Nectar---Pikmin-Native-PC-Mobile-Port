$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
$root=$PSScriptRoot
$profiles=@(Get-ChildItem -LiteralPath (Join-Path $root 'Profiles') -Filter '*.identity' | Sort-Object Name)
if(!$profiles.Count){throw 'No prepared phone-build profiles found.'}
$form=New-Object Windows.Forms.Form
$form.Text='Pikmin 1 - PC Test Partner';$form.ClientSize=New-Object Drawing.Size(620,330)
$form.StartPosition='CenterScreen';$form.FormBorderStyle='FixedDialog';$form.MaximizeBox=$false
$label=New-Object Windows.Forms.Label
$label.Text="Choose the P1 build currently INSTALLED on your phone.`r`nThis is a test partner, not the full PC game. Both devices need the same Wi-Fi/LAN."
$label.SetBounds(20,15,580,55);$form.Controls.Add($label)
$build=New-Object Windows.Forms.ComboBox;$build.DropDownStyle='DropDownList';$build.SetBounds(20,75,580,30)
foreach($profile in $profiles){[void]$build.Items.Add($profile.BaseName)}
$build.SelectedIndex=$profiles.Count-1;$form.Controls.Add($build)
$hostChoice=New-Object Windows.Forms.RadioButton
$hostChoice.Text='PC hosts: check the PHONE guest view (simple test scene)';$hostChoice.SetBounds(20,120,580,25)
$form.Controls.Add($hostChoice)
$joinChoice=New-Object Windows.Forms.RadioButton
$joinChoice.Text='PHONE hosts: PC joins (checks real phone host gameplay)';$joinChoice.SetBounds(20,155,580,25);$joinChoice.Checked=$true
$form.Controls.Add($joinChoice)
$notes=New-Object Windows.Forms.Label
$notes.Text="PC guest starts stationary; press M in its console to make it walk.`r`nP pauses/resumes, B simulates away/back, R marks Ready, Q disconnects.`r`nNo campaign progress is saved. Read START HERE before testing."
$notes.SetBounds(20,195,580,65);$form.Controls.Add($notes)
$start=New-Object Windows.Forms.Button;$start.Text='Start test partner';$start.SetBounds(360,275,240,35)
$start.DialogResult=[Windows.Forms.DialogResult]::OK;$form.Controls.Add($start);$form.AcceptButton=$start
if($form.ShowDialog() -ne [Windows.Forms.DialogResult]::OK){exit}
$selected=$profiles[$build.SelectedIndex].FullName
$mode=if($hostChoice.Checked){'--host'}else{'--join'}
$form.Dispose()
& (Join-Path $root 'nectar_practice_companion.exe') $mode $selected
Write-Host "`nTest partner finished. Read any result above. Press Enter to close."
[void](Read-Host)
