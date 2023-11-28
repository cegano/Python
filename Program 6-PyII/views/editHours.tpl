% rebase('layout.tpl', title='edit hours')

	<h3>Enter Employee ID and Hours Worked</h3><br>
	
	<form action="/editHours" method="post">
		
		<p><input name="eid" type="text" size="10"> Employee ID</p>
		<p><input name="hrs" type="text" size="10"> Hours Worked</p><br>
		<p><input type="submit"></p>
		
	</form>