<html><head></head><body>
<h1>Your Trip Data</h1>

<table class= 'table'>
	<tr><th>Trip Id</th><th>Username</th><th>Date</th><th>Destination</th><th>Miles</th><th>Gallons</th></tr>
		% for row in rows:
		
			<tr>
				<td>{{row[0]}}</td>
				<td>{{row[1]}}</td>
				<td>{{row[2]}}</td>
				<td>{{row[3]}}</td>
				<td>{{row[4]}}</td>
				<td>{{row[5]}}</td>
				
			</tr>
	
		%end
</tr>
</table>
</body></html>