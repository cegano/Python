% rebase('layout.tpl', title='departments')
 
	<h3>Get Payroll Data by Department</h3><br>
		<p>
		<form method='post' action='/byDepartment'>
		
		   Select Department: <select name='dept'>
		       <option value='shipping'>Shipping</option>
			   <option value='maintenance'>Maintenance</option>
			   <option value='environment'>Environment</option>
			   <option value='advertising'>Advertising</option>
		    </select><br>
			<br><br>
			<input type='submit'>
		<form>
		</p>
    <br>
