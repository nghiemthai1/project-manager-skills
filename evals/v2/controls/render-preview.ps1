Add-Type -AssemblyName System.Drawing
$bitmap = New-Object System.Drawing.Bitmap 1200,470
$canvas = [System.Drawing.Graphics]::FromImage($bitmap)
$canvas.Clear([System.Drawing.Color]::White)
$font = New-Object System.Drawing.Font 'Arial',11
$titleFont = New-Object System.Drawing.Font 'Arial',17
$dark = [System.Drawing.Brushes]::Black
$blue = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(48,94,150))
$amber = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(165,81,18))
$weekend = New-Object System.Drawing.SolidBrush ([System.Drawing.Color]::FromArgb(235,237,240))
$canvas.DrawString('Fictional Atlas | proposed single-specialist sequence',$titleFont,$dark,20,15)
$canvas.DrawString('Prepared 2026-09-16 | Monday-Friday, no holidays | bars show occupied working dates',$font,$dark,20,50)
$start = [datetime]'2026-10-05'
$left=300; $width=48
for ($i=0; $i -le 16; $i++) {
 $date=$start.AddDays($i); $x=$left+$i*$width
 if ($date.DayOfWeek -in @('Saturday','Sunday')) { $canvas.FillRectangle($weekend,$x,100,$width,310) }
 $canvas.DrawString($date.ToString('dd'),$font,$dark,$x+9,78)
 $canvas.DrawLine([System.Drawing.Pens]::LightGray,$x,100,$x,410)
}
$labels=@('AT-1 approved milestone','A - 2 working days','B - Fin, 4 working days','C - Fin, 3 working days','D - 1 working day','E - proposed milestone')
for ($r=0;$r -lt $labels.Count;$r++) { $canvas.DrawString($labels[$r],$font,$dark,20,(115+$r*48)) }
$rows=@(@(0,1),@(2,3,4,7),@(8,9,10),@(11))
for ($r=0;$r -lt 4;$r++) { foreach ($day in $rows[$r]) { $canvas.FillRectangle($blue,($left+$day*$width),(159+$r*48),$width,23) } }
foreach ($mark in @(@(9,124),@(14,364))) {
 $x=$left+$mark[0]*$width; $y=$mark[1]
 $points=[System.Drawing.Point[]]@([System.Drawing.Point]::new($x,$y-10),[System.Drawing.Point]::new($x+10,$y),[System.Drawing.Point]::new($x,$y+10),[System.Drawing.Point]::new($x-10,$y))
 $canvas.FillPolygon($amber,$points)
}
$canvas.DrawString('October 2026 | E: Oct 19 start-of-day vs AT-1: Oct 14 | +3 working days / +5 calendar days',$font,$dark,20,423)
$canvas.DrawString('No actual progress asserted. Static calendar fallback; Mermaid rendering not verified.',$font,$dark,20,445)
$bitmap.Save((Join-Path $PSScriptRoot 'atlas-gantt.png'),[System.Drawing.Imaging.ImageFormat]::Png)
$canvas.Dispose(); $bitmap.Dispose(); $font.Dispose(); $titleFont.Dispose(); $blue.Dispose(); $amber.Dispose(); $weekend.Dispose()
