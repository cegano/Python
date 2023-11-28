% rebase('layout.tpl', title='department')

<h3>Department: {{dept}}</h3><br>

<p><table class='table'>
<tr><th>Employee ID</th><th>Name</th><th>Wage</th><th>Hours Worked</th><th>Weekly Pay</th></tr>
%for row in rows:
	%for col in row:
		<td>{{col}}</td>
	%end
	</tr>
%end
</table>
</p>